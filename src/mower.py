class Mower:
    ALLOWED_VIEWS = ["DOWN", "RIGHT", "UP", "LEFT"]
    TERRAIN_SIZE = [30,55] #Dimension of the terrain

    def __init__(self):
        self.position = [0,0]
        self.mowedCases = 0
        self.view = "DOWN"
        self.visitedCases = set()
        self.terrain = [[0 for _ in range(self.TERRAIN_SIZE[0])] for _ in range(self.TERRAIN_SIZE[1])]
        self.visitedCases.add(tuple(self.position))

    def setView(self, new_view):
        if new_view not in self.ALLOWED_VIEWS:
            raise ValueError(f"Invalid view: {new_view}. Allowed values are: {self.ALLOWED_VIEWS}")
        self.view = new_view

    def turnLeft(self):
        viewIndex = self.ALLOWED_VIEWS.index(self.view)
        newIndex = (viewIndex + 1) % len(self.ALLOWED_VIEWS)
        self.view = self.ALLOWED_VIEWS[newIndex]

    def getView(self):
        return self.view

    def setPosition(self, new_position):
        self.position = new_position

    def getPosition(self):
        return self.position

    def isMowed(self, position):
        return self.terrain[position[1]][position[0]]

    def moveForward(self):
        if self.view == "DOWN":
            if self.position[1] + 1 < self.TERRAIN_SIZE[1]:
                self.position[1] += 1
        elif self.view == "RIGHT":
            if self.position[0] + 1 < self.TERRAIN_SIZE[0]:
                self.position[0] += 1
        elif self.view == "UP":
            if self.position[1] - 1 >= 0:
                self.position[1] -= 1
        elif self.view == "LEFT":
            if self.position[0] - 1 >= 0:
                self.position[0] -= 1

        self.visitedCases.add(tuple(self.position))

    def mow(self):
        current_position = tuple(self.position)
        if self.terrain[self.position[1]][self.position[0]] == 0:
            self.terrain[self.position[1]][self.position[0]] = 1
            self.mowedCases += 1
        self.visitedCases.add(current_position)

    def getMowedCount(self):
        return self.mowedCases

    def getVisitedCount(self):
        return len(self.visitedCases)

    def isComplete(self):
        return self.mowedCases == self.TERRAIN_SIZE[0] * self.TERRAIN_SIZE[1]