
import random

class Dice:

    sides = 0

    def __init__(self, totalSides):
        self.sides = totalSides

    def roll(self):
        return random.randint(1, self.sides);