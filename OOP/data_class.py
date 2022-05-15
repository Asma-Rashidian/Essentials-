"""
    Python data classes :
    1. Representation 
    2. Comparison 
    3. Adding default value
    4. ordering 
    5. Immutable data 
    6. Inheritance 
"""
"""
    by default data classes impelements __repr__()  to provide nice string representation 
    and __eq__() that can do basic object comparison
    you can add any type of methods in your data class 
"""


# ****************************************************************************************************
from dataclasses import dataclass
from typing import Any, any      #>>> used when you don't want to define an specific data type in your data class


@dataclass
class DataClassCard :
    name : Any 
    rank : str = 'asma'     # asma is the default value  if you want more complicated default values you should use default factory
    suit : str = 'asmaaa'


asma = DataClassCard()
print(asma)
queen_of_heart = DataClassCard("Q" , "Hearts")
print(queen_of_heart.rank)
print(queen_of_heart)
print(queen_of_heart == DataClassCard("Q" , "Hearts")) 

# comparisson to a regular data class 
class RegularCard :
    num = 0
    def __init__(self , rank , suit):
        self.rank = rank 
        self.suit = suit 
        RegularCard.num += 1 

    def __repr__(self):
        return "{}(rank='{}' , suit='{}')".format(self.__class__.__name__ , self.rank , self.suit)

    def __eq__(self,other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        
        return (self.rank , self.suit) == (other.rank , other.suit)

king = RegularCard("K" , "King")
print (king == RegularCard("K" , "King"))
print(king)

# ***********************************************************************************************************
# same as data class
# notice that the value of a name tuple is never changed it's amutable !!!
from collections import namedtuple 

NameTupleCard = namedtuple('NameTupleCard'  , ['rank' ,'suit'])
queen_of_hearts = NameTupleCard('Q' , 'Hearts')
print(queen_of_hearts.rank)

print(queen_of_hearts ==  NameTupleCard('Q','Heart'))

# *************************************************************************************************************
"""
    declare an attribute the same as data class 
    the Attrs project support features that data class doesnot support like converters and validators 
    it is not in standard library and needs external dependancies 
"""
import attr 

@attr.s
class AttrsCard :
    rank = attr.ib()
    suit = attr.ib()

queen_of_heartss = AttrsCard("Q" , "Hearts")
print(queen_of_heartss.rank)