import math


class Vektor():

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def add(self, vek):
        return (self.x + vel.x, self.y + vek.y)


    def sub(self, vek):
        return (self.x + vel.x, self.y + vek.y)


    def mag(self):
        return math.sqrt(self.x**2, self.y**2)


    def einheits_vektor(self):
        length = self.mag()

        return (self.x / length, self.y / length)