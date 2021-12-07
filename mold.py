import turtle
class Mold(turtle.Turtle):
    def __init__(self, shape, color, pos) -> None:
        turtle.Turtle.__init__(self, shape=shape)
        """Being mold, Initialize flying object"""
        self.speed(0)
        self.penup()
        self.color(color)
        self.goto(pos)

    def is_collided(self, other):
        """ Check collision of objects by 20 unit on the screen"""
        if (self.xcor() >= other.xcor() - 20 and 
        self.xcor() <= other.xcor() + 20 and
        self.ycor() >= other.ycor() - 20 and
        self.ycor() <= other.ycor() + 20):
            return True
        else:
            return False