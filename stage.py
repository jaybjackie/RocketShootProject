from border import Border
from turtle import Turtle
from enemy  import Enemy
from aircraft import Aircraft
from mold import Mold

import copy

class Stage:
    """Represent a stage for all objects"""

    def __init__(self) -> None:
        """Initialize a stage with the given border."""

    def init_screen(self):
        """Prepare a display window"""
        # Turtle object as a painter
        self.__painter = Turtle()

        # set the turtle display screen to 900x600 px
        self.__painter.screen.setup(900, 600)

        # set display screen
        self.__painter.forward(0)
        self.__painter.screen.bgcolor('black')
        self.__painter.setundobuffer(1)
        self.__painter.screen.tracer(1)
        self.__painter.speed(0)
        self.__painter.hideturtle()
        self.__painter.penup()