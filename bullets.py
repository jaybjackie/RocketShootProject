from turtle import shapesize
from mold import Mold
import os

class Bullets(Mold):
    def __init__(self, shape, color, pos, player) -> None:
        super().__init__(shape, color, pos)
        self.shapesize(stretch_wid = 0.3, stretch_len=0.5, outline= None)
        self.speed = 14
        self.setheading(0)
        self.goto(pos)
        self.status = 'ready'
        self.pilot = player
    
    def firing(self):
        if self.status == 'ready':
            # play shooting sound
            os.system("afplay sfx/laser-gun-shot.wav&")
            self.goto(self.pilot.position())
            self.status = 'firing'

    def move(self):
        """ Move when Status is firing"""
        if self.status == 'firing':
            self.setx(self.xcor() + self.speed)
            if self.xcor() >= 405:
                self.goto(-800,800)
                self.status = 'ready'