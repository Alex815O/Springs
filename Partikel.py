import arcade

class Partikel():

    def __init__(self, vec, radius, anker=False):

        self.vec = vec
        self.radius = radius
        self.anker = anker


    def draw(self):
        arcade.draw_circle_filled(self.vec.x, self.vec.y, self.radius, arcade.color.BLEU_DE_FRANCE, 4)

    
