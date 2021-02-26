import arcade
from Partikel import Partikel
from Spring import Spring
from Vektor import Vektor

class Base(arcade.Window):

    gravity = Vektor(0, -0.5)
    doUpdate = True

    def __init__(self, width, height):
        super().__init__()
        

    def setup(self):
        arcade.set_background_color(arcade.color.PURPLE)

        k = 0.001
        length = 1
        anz_balls = 15

        self.balls = []
        self.springs = []

        self.balls.append(Partikel(Vektor(arcade.get_window().get_size()[0]//anz_balls*2, arcade.get_window().get_size()[1]-100), 15, True))

        for i in range(1, anz_balls):
            self.balls.append(Partikel(Vektor(arcade.get_window().get_size()[0]//anz_balls*i, arcade.get_window().get_size()[1]-100), 8))
            self.springs.append(Spring(self.balls[i-1], self.balls[i], k, length))
        
        self.balls.append(Partikel(Vektor(arcade.get_window().get_size()[0]//anz_balls*(anz_balls-2), arcade.get_window().get_size()[1]-100), 15, True))
        self.springs.append(Spring(self.balls[-2], self.balls[-1], k, length))
        



    def on_draw(self):
        arcade.start_render()

        for spring in self.springs:
            spring.draw()
        
        for ball in self.balls:
            if ball.anker:
                ball.draw()

    
    def on_update(self, delta_time):
        for spring in self.springs:
            spring.update()

        for ball in self.balls:
            if not ball.anker:
                ball.vec = Vektor.add(ball.vec, Base.gravity)
        
        
    def on_mouse_press(self, x, y, b, m):
        self.balls[len(self.balls)//2].vec.x = x
        self.balls[len(self.balls)//2].vec.y = y
        self.balls[len(self.balls)//2].anker = True
        Base.doUpdate = False


    def on_mouse_release(self, x, y, b, m):
        Base.doUpdate = True

    def on_mouse_drag(self, x, y, dx, dy, button, modifiers):
        self.balls[len(self.balls)//2].vec.x = x
        self.balls[len(self.balls)//2].vec.y = y
        



b = Base(400, 500)
b.setup()
arcade.run()