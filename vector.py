### This code is from week10 assignment ###

class Vector:
    """Define a vector in 2D space."""

    def __init__(self, x=0,y=0) -> None:
        self.x = x
        self.y = y
    
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("The x attribute must be a number")          
        self.__x = x
    
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, (int, float)):
            raise TypeError("The y attribute must be a number")          
        self.__y = y
        
    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"