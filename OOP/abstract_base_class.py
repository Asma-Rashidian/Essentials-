"""
    *** Part 3 ***
    Provide a base class that define a template for other classes to inherite from 
    we want to force every shape calculat calcArea , 
    and we want to prevent the graphic shape class itself from being instantiated on its own
"""
from abc import ABC , abstractmethod
# abc >> Abstract Base Class

class GraphicShape (ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle (GraphicShape):
    def __init__(self , radius):
        self.radius = radius

    def calcArea(self):
        return 3.14*(self.radius ** 2)

class Square (GraphicShape):
    def __init__(self , side):
        self.side = side 

    def calcArea(self):
        return self.side ** 2

# g = GraphicShape() >>> get an error because you cant inherit from an abstract class
cir = Circle(3)
print(cir.calcArea())