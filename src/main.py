import random
from deap import creator, base, tools, algorithms

# creator.create("FitnessMin", base.Fitness, weights=(-1.0,))  # Minimisation de la fitness
# creator.create("Individual", list, fitness=creator.FitnessMin)
#
# toolbox = base.Toolbox()
# toolbox.register("attr_move", lambda: random.choice([(0,1), (1,0), (0,-1), (-1,0)]))
# toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_move, n=100)
# toolbox.register("population", tools.initRepeat, list, toolbox.individual)
#
# toolbox.register("mate", tools.cxTwoPoint)
# toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.2)
# toolbox.register("select", tools.selTournament, tournsize=3)
# toolbox.register("evaluate", fitness_function)



def main():
    # population initiale
    #population = toolbox.population(n=100)

    # Paramètres de l'algorithme évolutionnaire
    ngen = 50  # Nombre de générations
    cxpb = 0.7  # Probabilité de croisement
    mutpb = 0.2  # Probabilité de mutation


if __name__ == '__main__':
    main()