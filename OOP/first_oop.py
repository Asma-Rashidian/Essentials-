"""
    *** Part 1***
    Object Oriented Programming Language  >>> OOP

        OOP Terms 
            classes : a blueprint of creating objects of a prticular type 
            methods : regular functions that are part of class 
            attributes : variables that hold data as a part of class
            object : a specific instance of a class 
            inheritance : which class can inherit capabilities of another class
            composition : buildings of complex objects out of other objects 


"""
# class without inheritance 
class Book :
    
    # properties defined at the class level are shared by all instance 
    BOOK_TYPES = ("HARDCOVER" , "PAPERBACK" , "EBOOk")

    # Initializer  of new object >> it is not called  constructor  like java 
    # self is just naming convention 
    def __init__(self , title , author , pages , price , booktype):
        # title , price , author , pages are instance atributes 
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
       # to declare a parameter that can only be seen inside the class
       # This makes you sure that the subclasses don't use the same name for an attribute that you have already used 
        self.__secret = "This is a secret attribute"
    
        if (not booktype in Book.BOOK_TYPES ):
           raise ValueError(f"{booktype} is not valid")
        else:
            self.booktype = booktype


    # create a class method  >>> use class method decorator
    @classmethod
    def getBookTypes (cls):
        return cls.BOOK_TYPES
    

    # double-underscore properties are hidden from other classes 
    __booklist = None 

    # make a class modified without initialization ?
    @staticmethod
    def getBookList ():
        if Book.__booklist == None :
            Book.__booklist =[]
        
        return Book.__booklist


    def getPrice (self):
        
        # check we have a attribute or not 
        if hasattr(self , "_discount"):
            return self.price - self.price * self._discount
        else :
            return "The Price is {}".format(self.price)

    def setDicount(self , amount):

        # _discount : means other developers a hint that this attribute can't be used out of class and its internal to the class
        self._discount = amount


    


object1  = Book("The Tale of Two Cities" , "Charlz Dikens" , 600 , 100 , "PAPERBACK")
print(object1.getPrice())
object1.setDicount(0.25)
print(object1.getPrice())

# print(object1.__secret)      # >>> the error is "'Book' object has no attribute '__secret'"
# Name  Mangling : This is called name mangling. The reason for this feature is to prevent sub classesfrom inadvertently overriding the attribute but other classes can subvert this simply by using the class name

print(object1._Book__secret)

# Check an object is instance of a class 
print(isinstance(object1 , Book))


print("Book Types : " , Book.getBookTypes())

thebooks = Book.getBookList()
thebooks.append(object1)
print(thebooks)

