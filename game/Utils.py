import random
from game.objects import Object


def generate(num: int, resolution: tuple[int]):
    items = []
    for i in range(num):
        items.append(Object(int(random.random()*resolution[0]),int(random.random()*resolution[1]),16,16))
    return items