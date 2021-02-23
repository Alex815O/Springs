import arcade

class Base(arcade.Window):

    def __init__(self, width, height):
        super().__init__()
        

    def setup(self):
        arcade.set_background_color(arcade.color.PURPLE_NAVY)

        self.k = 0.01
        self.length = 100
        self.velocity = 0.0

        self.ball = [arcade.get_window().get_size()[0]//2, arcade.get_window().get_size()[1]//2]
        self.ball_radius = 30

        self.anker = (arcade.get_window().get_size()[0]//2, self.ball[1]+self.length)

        self.gravity = (0, -10)



    def on_draw(self):
        arcade.start_render()
        arcade.draw_line(self.anker[0], self.anker[1], self.ball[0], self.ball[1], arcade.color.WHITE_SMOKE)
        arcade.draw_circle_filled(self.ball[0], self.ball[1], self.ball_radius, arcade.color.BLEU_DE_FRANCE)

    
    def on_update(self, delta_time):
        
        x = (self.anker[1] - self.ball[1]) - self.length
        force_spring = self.k * x

        self.ball[1] += force_spring

        self.velocity += force_spring
        self.ball[1] += self.velocity


    def on_mouse_drag(self, x, y, dx, dy, button, modifiers):
        self.ball[1] = y

b = Base(400, 800)
b.setup()
arcade.run()