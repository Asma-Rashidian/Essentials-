"""
    *** Part 6 ***
    the differance of composition and inheritance is shown in image comVsinh.jpeg

""" 
class Book:
    def __init__(self , title , price , author = None):
        self.title = title 
        self.price = price

        self.chapters = []

        self.author = author 

    def addchapter(self , chapter):
        self.chapters.append(chapter)

    def getbookpage(self):
        count = 0 
        for ch in self.chapters:
            count += ch.pagecount
            return count


# extract authour information into it's own class
class Author :
    def __init__(self , fname , lname ):
        self.fname = fname 
        self.lname = lname 

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Chapters :
    def __init__(self , name , pagecount):
        self.name = name 
        self.pagecount = pagecount



auth = Author( "Leo" , "Tolstoy")
b1 = Book("War and Peace" , 39.0 , auth)
b1.addchapter(Chapters("chapter1" , 125))
print(b1.getbookpage())





