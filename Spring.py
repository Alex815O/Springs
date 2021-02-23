import arcade
from Vektor import Vektor

class Spring():

    def __init__(self, pa, pb, k, length):
        self.pa = pa
        self.pb = pb

        self.spring_vec = Vektor.sub(pb.vec, pa.vec)
        self.k = k
        self.length = length
        self.velocity = Vektor(0, 0)



    def draw(self):
        arcade.draw_line(self.pa.vec.x, self.pa.vec.y, self.pb.vec.x, self.pb.vec.y, arcade.color.WHITE_SMOKE)
        

    def update(self):
        
        self.spring_vec = Vektor.sub(self.pb.vec, self.pa.vec)

        x = self.spring_vec.mag() - self.length
        
        force = self.spring_vec.normalise().mult_value(-self.k * x)

        self.velocity = Vektor.add(self.velocity, force)
        self.pb.vec = Vektor.add(self.pb.vec, self.velocity)

        self.velocity = self.velocity.mult_value(0.99)

        

