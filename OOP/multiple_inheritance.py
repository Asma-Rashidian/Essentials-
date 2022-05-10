"""
    *** Part 4 ***
    inherit more than 1 base class 
"""

# we mostly use multiple inheritance in Interfaces 

class A:
    def __init__(self) :
        super().__init__()
        self.foo = "foo"
        # define same attribute in class A , B
        self.name = "Class A"

class B : 
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        # define same attribute in class A , B
        self.name = "Class B"

class C(A , B):
    def __init__(self):
        super().__init__()

    def showProp(self):
        print(self.bar  , self.foo)

        """
            when you call a method or access an attribute in Python, 
            the Python interpreter uses something called the method
            ** resolution order to look it up ** in the class. 
            So the lookup starts in the current class, in this case Class C,
            which doesn't define the name attribute.
            So then Python looks in the superclasses in the order in which they are defined from left to right.
            So since Class A is listed first, that's why we're seeing the Class A string in the output.
        """
        print(self.name)

c = C().showProp()

# See Method Resolution Order 
print(C.__mro__)

