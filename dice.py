
import random

class Dice:

    sides = 0

    def __init__(self, totalSides):
        self.sides = totalSides

    def roll(self):
        return random.randint(1, self.sides)

    def rollAndAdd(self, times):
        temp = 0

        for i in range(times):
            temp = temp + self.roll()

        return temp

    def rollAndAverage(self, times):
        temp = 0

        for i in range(times):
            temp = temp + self.roll()

        return temp / times

