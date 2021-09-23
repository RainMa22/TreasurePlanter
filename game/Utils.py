import random
from game.objects import GridBasedObject


def generate(num: int, grid: list, resolution):
    items = []
    for i in range(num):
        items.append(GridBasedObject(grid,int(random.random()*resolution[0]),int(random.random()*resolution[1]),16,16))
    return items