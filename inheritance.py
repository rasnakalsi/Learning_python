## UNCOMMENT THE COMMENTED CODE BELOW-- TO RUN CODE WITHOUT INHERITANCE
# class Book:
#     def __init__(self,title,author,price,pages):
#         self.title=title
#         self.author=author
#         self.pages=pages
#         self.price=price

# class Magazine:
#     def __init__(self,title,publisher,price,period):
#         self.title=title
#         self.price=price
#         self.publisher=publisher
#         self.period=period

# class Newspaper:
#     def __init__(self,title,publisher,price,period):
#         self.title=title
#         self.price=price
#         self.period=period
#         self.publisher=publisher

# b1=Book("Atomic habbits","Rasna",320,33)
# n1=Newspaper ("The Tribune","Tribune",334,1)
# m1=Magazine("Outlook","Rinku",400,300)

# print(b1.author)
# print(n1.publisher)
# print(b1.price,n1.price,m1.price)

## CODE SHOWING USE OF INHERITANCE-- COMMON ELEMENTS ARE PLACED AT  A COMMON BASE CLASS

##BASE CLASS#1 -- CONTAINING TITLE AND PRICE

class Publication:
    def __init__(self,title,price):
        self.title=title
        self.price=price

class Periodical(Publication):
    def __init__(self,title,price,publisher,period):
        super().__init__(title,price)
        self.publisher=publisher
        self.period=period


class Book(Publication):
    def __init__(self,title,author,price,pages):
        super().__init__(title,price)
        self.pages=pages
        self.author=author


class Magazine(Periodical):
    def __init__(self,title,publisher,price,period):
        super().__init__(title,price,publisher,period)

class Newspaper(Periodical):
    def __init__(self,title,publisher,price,period):
        super().__init__(title,price,publisher,period)

b1=Book("Atomic habbits","Rasna",320,33)
n1=Newspaper ("The Tribune","Tribune",334,1)
m1=Magazine("Outlook","Rinku",400,300)

print(b1.author)
print(n1.publisher)
print(b1.price,n1.price,m1.price)