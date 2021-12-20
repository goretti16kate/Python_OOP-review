class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self,title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__seceret = "This is a secret attribute"

    # TODO: create instance methods
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        #give a hint that the method is only intended to be used in the class
        self._discount= amount 

# TODO: create some book instances
b1 = Book("War and Peace","Leo Tolstoy", 1225, 39.95)
b2 = Book ("The Catcher in the Rye","JD Selinger", 234, 29.95)

# TODO: print the price of book1
print(b1.getprice())

# TODO: try setting the discount
print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())

# TODO: properties with double underscore are hidden
print(b2._Book__seceret)