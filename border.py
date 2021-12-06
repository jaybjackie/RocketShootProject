import copy
from vector import Vector
from read import Read

class Border:
    """
    Define a border in 2D space with the lower-left corner, width, and height.
    And display status; score
    """

    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height
        
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
        """ Draw the border by given width and height """
        painter.penup()
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
        painter.penup()

    def show_status(self, painter, player):
        """ Display score and player lives on the screen """
        painter.undo()
        msg = f'Score: {player.score}'
        painter.penup()
        painter.goto(-400,275)
        painter.write(msg + f'      lives: {player.lives}', font=("Arial", 16,"normal"))
        
    def display_gameover(self,painter, player):
        """ Display gameover when the game is over """
        painter.pendown()
        painter.undo()
        msg = f'GAME OVER\nSCORE : {player.score}'
        painter.penup()
        painter.goto(0, 100)
        painter.write(msg,align='center', font=("Arial", 22, "bold"))
        painter.goto(250,-265)
        painter.write('click to exit or exit button',align='left', font=("Arial", 12, "normal"))
        painter.hideturtle()
    
    def display_rank(self, painter, player_name, score):
        """ Display player name and their score on the screen """
        pen = Read(name=player_name, score=score)
        # insert player name and score to database
        pen.insert()
        painter.undo()
        painter.goto(0, 70)
        painter.write('Leadership',align='center', font=('Arial', 20,'bold'))
        # top_player example [('Hibara', 9900), ('conan', 9000), ('Run', 4000)]
        top_player = pen.get_top() 
        for p in range(len(top_player)):
            painter.goto(0, 65-((p+1)*20))
            name, score = top_player[p][0], top_player[p][1] # name and score
            msg = f"{name}      {str(score)}"
            painter.write(msg,align='center',font=("Arial", 16, "bold"))
        painter.hideturtle()