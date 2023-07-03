from dataclasses import dataclass

@dataclass 
class Book:
    title:str
    author:str
    pages:int
    price:float
    description:str

    def bookinfo(self):
        return f"{self.title} by {self.author}"

    def __post_init__(self):
        self.description=f"{self.title} by {self.pages} ,{self.pages} pages"





b1=Book("War and Peace","Leo Tolstoy",200,40)
b2=Book("The Catcher in the Rye","JD Salinger",300,100.31)
b3=Book("War and Peace","Leo Tolstoy",200,40)
print(b1.description)
print(b2)


# print(b1==b3)
# print(b1==b2)

# b1.title="Atomic Habbits"
# b1.price=0
# print(b1)