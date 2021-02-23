import arcade

class Partikel():

    def __init__(self, vec, radius):

        self.vec = vec
        self.radius = radius


    def draw(self):
        arcade.draw_circle_filled(self.vec.x, self.vec.y, self.radius, arcade.color.BLEU_DE_FRANCE)

    
