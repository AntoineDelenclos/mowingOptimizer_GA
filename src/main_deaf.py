import random
from deap import base, creator, gp, tools, algorithms
from src.mower import Mower

# Primitives pour la programmation génétique
def move_forward(mower):
    mower.moveForward()

def turn_left(mower):
    mower.turnLeft()

def mow_grass(mower):
    mower.mow()


# Configuration de DEAP, creation de la fitness fonction
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMax)

# Primitives basées sur un Mower
pset = gp.PrimitiveSet("MAIN", 1)  # Le programme prend 1 argument : un Mower, une tondeuse
pset.renameArguments(ARG0='mower') #on renomme l'argument mower
#on ajoute les actions pouvant être effectués par la tondeuse
pset.addPrimitive(move_forward, 1)
pset.addPrimitive(turn_left, 1)
pset.addPrimitive(mow_grass, 1)

# Toolbox ne fonctionne pas du tout
toolbox = base.Toolbox()
toolbox.register("expr", gp.genFull, pset=pset, min_=1, max_=3)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=pset)

# Évaluation --->>>> ne fonctionne pas du tout
def evaluate(individual):
    mower = Mower()
    func = toolbox.compile(expr=individual)
    movements = 0

    for _ in range(500):  # Nombre maximum de mouvements
        func(mower)
        movements += 1
        if mower.isComplete():  # Si toutes les cases sont tondues
            break

    # Fitness = cases tondues
    return mower.getMowedCount()


toolbox.register("evaluate", evaluate)
toolbox.register("select", tools.selTournament, tournsize=3)  #selection (3 individus sont comparés)
toolbox.register("mate", gp.cxOnePoint)   #croisement, mélange deux arbres
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr, pset=pset)     #mutation, remplace une partie de l'arbre par une nouvelle arboresence


# Évolution
def main():
    random.seed(42)
    population = toolbox.population(n=300)
    hof = tools.HallOfFame(1)  #conservation du meilleur individu


    stats = tools.Statistics(lambda ind: ind.fitness.values[0])
    stats.register("fitness moyenne", lambda pop: round(sum(pop) / len(pop), 2))
    stats.register("écart type de la fitness", lambda pop: round(
        (sum((x - sum(pop) / len(pop)) ** 2 for x in pop) / len(pop)) ** 0.5, 2))
    stats.register("fitness minimum", min)
    stats.register("fitness maximum", max)

    #effectue 40 générations avec un taux de croisement de 50%, 20% de mutation
    algorithms.eaSimple(
        population, toolbox,
        cxpb=0.5, mutpb=0.2, ngen=40,
        stats=stats, halloffame=hof, verbose=True
    )

    # Meilleure solution avec la fitness affichée
    best = hof[0]
    print("Meilleur programme de tonte:", best)
    print("Fitness:", evaluate(best))

    # Visualisation la grille finale
    mower = Mower()
    func = toolbox.compile(expr=best)
    for _ in range(500):
        func(mower)
        if mower.isComplete():
            break

    for row in mower.terrain:
        print("".join(["#" if cell == 1 else "." for cell in row]))

if __name__ == "__main__":
    main()