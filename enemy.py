from turtle import xcor
from mold import Mold

class Enemy(Mold):
    def __init__(self, shape, color, pos) -> None:
        super().__init__(shape, color, pos)
        self.shapesize(stretch_wid=2, stretch_len=2, outline=None)
        self.level = 1
        self.speed = 8
        self.setheading(180)

    def move(self):
        self.setx(self.xcor() - self.speed)