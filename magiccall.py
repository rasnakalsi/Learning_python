class Book:
    def __init__(self,title,author,price):
        super().__init__()
        self.title=title
        self.author=author
        self.price=price

    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"
    
    #defining magic call method
    def __call__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    

b1=Book("Atomic Habbits","Rasna ",213)
b2=Book("Rich Dad Poor Dad","Rinku",323)
print(b1) ## using magic __str__ fn
b1("Superfoods","Rasna ",21300) ##using magic call to modify the object
print(b1)