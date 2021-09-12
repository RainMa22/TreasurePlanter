class Object:
    def __init__(self, x=0, y=0, width=0, height=0, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def act(self):
        pass


class GridBasedObject(Object):
    def __init__(self, grid: list, x=0, y=0, width=0, height=0, color=(0, 0, 0)):
        super(GridBasedObject, self).__init__(x, y, width, height, color)
        self.x = int(x / len(grid[0])) * len(grid[0])
        self.y = int(y / len(grid)) * len(grid)


class Plant(Object):
    def __init__(self, x=0, y=0, width=0, height=0, color=(0, 0, 0), frames=360):
        super(Plant, self).__init__(x, y, width, height, color)
        self.frames = frames

    def act(self):
        super(Plant, self).act()
        self.frames -= 1
        if self.frames <= 1:
            self.color = (255, 0, 255)
