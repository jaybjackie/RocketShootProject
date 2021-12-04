from turtle import shapesize, speed
from mold import Mold
from aircraft import Aircraft
import copy

class Bulltes(Mold):
    def __init__(self, shape, color, pos, player) -> None:
        super().__init__(shape, color, pos)
        self.shapesize(stretch_wid = 0.3, stretch_len=0.5, outline= None)
        self.speed = 20
        self.setheading(0)
        self.goto(pos)
        self.status = 'ready'
        self.pilot = player
    
    def firing(self):
        if self.status == 'ready':
            self.goto(self.pilot.position())
            self.status = 'firing'

    def move(self):
        if self.status == 'firing':
            self.setx(self.xcor() + self.speed)
            if self.xcor() >= 405:
                self.goto(-800,800)
                self.status = 'ready'
    
