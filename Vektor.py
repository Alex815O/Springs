import math


class Vektor():

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def add(vek1, vek2):
        return Vektor(vek1.x + vek2.x, vek1.y + vek2.y)


    def sub(vek1, vek2):
        return Vektor(vek1.x - vek2.x, vek1.y - vek2.y)
 
    
    def mult(vek1, vek2):
        return Vektor(vek1.x * vek2.x, vek1.y * vek2.y)


    def mult_value(self, value):
        return Vektor(self.x * value, self.y * value)


    def mag(self):
        return math.sqrt(self.x**2 + self.y**2)


    def normalise(self):
        length = self.mag()

        return Vektor(self.x / length, self.y / length)


    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"