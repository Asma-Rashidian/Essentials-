"""
    *** Part 2 ***
"""
class Publication :
    def __init__(self , title , price ):
        self.title = title 
        self.price = price 

class Periodiacal(Publication):
     def __init__(self , title , price , period , publisher):
        super().__init__(title , price)
        self.period = period 
        self.publisher = publisher 


class Book (Publication):
    def __init__ (self , title , author , pages, price):
        # price , title  >>> inheritance of publication
        super().__init__(title , price)
        self.author = author 
        self.pages = pages 
       
    

class Magazine (Periodiacal):
    def __init__(self , title , publisher , price , period) :
        # price , title  >>> inheritance of periodical
        super().__init__(title , price , period , publisher )
        



class Newspaper (Periodiacal):
    def __init__(self , title , publisher , price , period) :
        # price , title  >>> inheritance of periodiacal
        super().__init__(title , price , period , publisher )
        