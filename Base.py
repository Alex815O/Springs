import arcade
from Partikel import Partikel
from Spring import Spring
from Vektor import Vektor

class Base(arcade.Window):

    gravity = Vektor(0, -9.89)
    doUpdate = True

    def __init__(self, width, height):
        super().__init__()
        

    def setup(self):
        arcade.set_background_color(arcade.color.PURPLE_NAVY)

        k = 0.01
        length = 200

        self.ball = Partikel(Vektor(arcade.get_window().get_size()[0]//2, arcade.get_window().get_size()[1]//2), 30)

        self.anker = Partikel(Vektor(arcade.get_window().get_size()[0]//2, self.ball.vec.y + length), 10)

        self.spring = Spring(self.anker, self.ball, k, length)
        



    def on_draw(self):
        arcade.start_render()

        self.spring.draw()
        self.ball.draw()
        self.anker.draw()

    
    def on_update(self, delta_time):
        if Base.doUpdate:
            self.spring.update()
            self.ball.vec = Vektor.add(self.ball.vec, Base.gravity)
        
        
    def on_mouse_press(self, x, y, b, m):
        self.ball.vec.x = x
        self.ball.vec.y = y
        Base.doUpdate = False


    def on_mouse_release(self, x, y, b, m):
        Base.doUpdate = True

    def on_mouse_drag(self, x, y, dx, dy, button, modifiers):
        self.ball.vec.x = x
        self.ball.vec.y = y



b = Base(400, 800)
b.setup()
arcade.run()