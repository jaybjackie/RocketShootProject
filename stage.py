from turtle import Turtle

class Stage:
    """ Initailize display window"""

    def init_screen(self):
        """ Prepare a display window """
        # Turtle object as a painter
        self.__painter = Turtle()

        # set the turtle display screen to 900x600 px
        self.__painter.screen.setup(900, 600)

        # set display screen
        self.__painter.hideturtle()
        self.__painter.penup()
        self.__painter.forward(0)
        # set bg color
        self.__painter.screen.bgcolor('black')
        # change background picture
        self.__painter.screen.bgpic("outer space.gif")
        # set title
        self.__painter.screen.title("Rocket Shoot Game")
        # set undo step by 1
        self.__painter.setundobuffer(1)
        self.__painter.screen.tracer(0)
        self.__painter.speed(0)