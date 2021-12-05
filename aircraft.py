import turtle
from mold import Mold

class Aircraft(Mold):
    def __init__(self, shape, color, pos) -> None:
        super().__init__(shape, color, pos)
        self.shapesize(stretch_wid=1.3, stretch_len= 0.8, outline=None)
        self.speed = 10
        # limit of player lives
        self.lives = 3

    def move(self):
        self.forward(0)
        # print(self.pos())

    def move_up(self):
        self.sety(self.ycor() + self.speed)
        # Top player border
        if self.ycor() > 260:
            self.sety(260)

    def move_down(self):
        self.sety(self.ycor() - self.speed)
        # Bottom player border
        if self.ycor() < -260:
            self.sety(-260)

    def move_forward(self):
        self.setx(self.xcor() + self.speed)
        # Right player border
        if self.xcor() > -300:
            self.setx(-300)

    def move_backward(self):
        self.setx(self.xcor() - self.speed)
        # Left player border
        if self.xcor() < -400:
            self.setx(-400)
        


