class Book:
    def __init__(self,title,author,price):
        super().__init__()
        self.title=title
        self.author=author
        self.price=price

    def __str__(self):
        return f"{self.title} by {self.author} costs {self.price}"

    def __repr__(self):
        return f"title={self.title},author={self.author},costs={self.price}"

b1=Book("Atomic Habits","Rasna",210)
b2=Book("Rich dad poor dad","Rinku",190)
print(b1)
print(b2)
print(str(b1))
print(repr(b1))