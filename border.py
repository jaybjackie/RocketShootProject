import copy
import turtle
from vector import Vector

class Border:
    """
    Define a border in 2D space with the lower-left corner, width, and height.
    And display status; score
    """

    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height
        self.score = 0
        
    def __repr__(self):
        return (f"Border(corner={self.corner},"
                f" width={self.width}, height={self.height})")

    @property
    def corner(self):
        return self.__corner

    @corner.setter
    def corner(self, corner):
        if not isinstance(corner, Vector):
            raise TypeError ("corner must be a Vector object")
        self.__corner = copy.copy(corner)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, (int, float)):
            raise TypeError("width must be a number")
        if width <= 0:
            raise ValueError("width must be greater than zero")     
        self.__width = width
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, (int, float)):
            raise TypeError("height must be a number")
        if height <= 0:
            raise ValueError("height must be greater than zero")     
        self.__height = height
    

    @property
    def left(self):
        """ Read-Only properties """
        return self.corner.x

    @property
    def right(self):
        """ Read-Only properties """

        return self.corner.x + self.width
    
    @property
    def bottom(self):
        """ Read-Only properties """

        return self.corner.y

    @property
    def top(self):
        """ Read-Only properties """
        return self.corner.y + self.height

    @property
    def sides(self):
        """ Read-Only properties """
        return (self.left, self.right, self.bottom, self.top)
 
    def draw(self, painter):
        # use the painter object (a turtle) to draw the border
        """ Draw the border and suppose Width and Height are the same value """
        painter.speed(0)
        painter.setheading(0)
        painter.goto(self.left - (self.width/2)*0.9, self.bottom - (self.height/2)*0.9)
        painter.pensize(2)
        painter.pencolor("white")
        painter.pendown()
        for _ in range(2):
            painter.forward(self.width*0.9)
            painter.left(90)
            painter.forward(self.height*0.9)
            painter.left(90)
        painter.hideturtle()
        painter.pendown()

    def show_status(self, painter, player):
        painter.undo()
        msg = f'Score: {self.score}'
        painter.penup()
        painter.goto(-400,275)
        painter.write(msg + f'lives: {player.lives}', font=("Arial", 16,"normal"))
        
    def display_gameover(self,painter, player):
        painter.undo()
        msg = f'GAME OVER\n{self.score}'
        painter.penup()
        painter.goto(-20,20)
        painter.write(msg, font=("Arial", 20,"normal"))