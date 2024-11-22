class Mower:
    ALLOWED_VIEWS = ["DOWN", "RIGHT", "UP", "LEFT"]
    TERRAIN_SIZE = [30,55] #Dimension of the terrain

    def __init__(self):
        self.position = [0,0]
        self.mowedCases = 0
        self.view = "DOWN"
        self.terrain = [[0 for i in range(self.TERRAIN_SIZE[0])] for j in range(self.TERRAIN_SIZE[1])]

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
        return self.terrain[position[0]][position[1]]

    def moveForward(self):
        match self.view:
            case "DOWN":
                self.position[1] += 1
            case "RIGHT":
                self.position[0] += 1
            case "UP":
                self.position[1] -= 1
            case "LEFT":
                self.position[0] -= 1

    def mow(self):
        self.terrain[self.position[0]][self.position[1]] = 1