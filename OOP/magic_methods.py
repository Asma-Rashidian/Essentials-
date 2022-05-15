"""
    *** Part 7 ***
    these magic methods help us to emulate some built in behaviour 
    magic methods are always surrounded by double underescore so called 'dunder'

    1. Your classes can override these methods to customize a variety of behavior and make them act just like Python's built-in classes. 
    2. Using these methods, you can customize how your objects are represented as strings, both for display to the user and for debugging purposes
    3. You can control how attributes are accessed on an object both for when they are set, and for when they are retrieved.
    4. You can add capabilities to your classes that enable them to be used in expressions such as testing for equality, or other comparison operations like greater than or less than.

"""
class Employee :
    raise_amt = 1.04

    def __init__(self, first , last , pay):
        self.first = first 
        self.last = last
        self.pay = pay 
        self.email = first + '.' + last +"@gmail.com" 

    def fullname (self):
        return f"{self.first} {self.last}"

    def apply_raise (self):
        self.pay = int(self.pay + self.raise_amt)

    # Unambiguous represntation of object >> with no vague >> used for debugging and loging and things like that 
    def __repr__(self):
        return "Employee ('{}' , '{}' , '{}')".format(self.first , self.last , self.pay)  # it is how we create an object 

    # is more readable representation of an object and is ment to be used as a display to an end user
    def __str__(self):
        return '{} - {}'.format(self.first , self.last) 

    # calculate sum of salary
    def __add__(self , other):
        return self.pay + other.pay

    # used for example when we want to return total character in full name 
    def __len__(self):
        return len(self.fullname())




emp1 = Employee("Asma" , "Rashidian" , 100)
emp2 = Employee("Ali" , "Rashidian" , 200)

print(emp1) # The output is <__main__.Employee object at 0x7f85d9f61e80>
# the print output is vague so we add __repr__ so the out of print will be "Employee ('Asma' , 'Rashidian' , '100')"
# and when we add __str__ it will print >> Asma - Rashidian
print(repr(emp1))
print(str(emp1))


# ***************************************************
print(1+2)
print(int.__add__(1,2))
print(str.__add__('a' , 'b'))

#uses __add__ method
print(emp1 +emp2 )
# **************************************************** 

print(len("asma"))
print('asma'.__len__())
print(len(emp1))

# ****************************************************
"""
return NotImplemented  >>>  we dont want to throw an error because the other object might know how to handle that operation and if 
both don't know how to handle it throw an error 

"""