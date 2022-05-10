"""
    *** Part 5 ***
    Python doesn't have explicit language suport for interface 
    you can think interface is a kind of promise , by implementing an interface a class provide a kind of promise and 
    contract to provide a certain behavior or cappability.

"""

from abc import ABC, abstractmethod

# a very small focused class and repersent it self as a JSON
class JSONify (ABC):
    @abstractmethod
    def toJSON (self):
        pass


class GraphicShape (ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle (GraphicShape , JSONify):
    def __init__(self , radius):
        self.radius = radius

    def calcArea(self):
        return 3.14*(self.radius ** 2)

    def toJSON(self):
        return f"{{\"square\" : {str(self.calcArea())}}}"

class Square (GraphicShape):
    def __init__(self , side):
        self.side = side 

    def calcArea(self):
        return self.side ** 2


cir1 = Circle(5)
print(cir1.toJSON())