# class of the library 
# for rending books 
# adding books 
# updating books 
# delete books from the library 
class Library:
    # class memebers 
    def __init__(self,books):
        self.books=[]
    




    def add(self) :
        # we first create the library 
        
        while True :
            book = input (" enter the book name :")
            self.books.append(book)
            print (" the book is ",book)
            print (self.books)
            
                 
        