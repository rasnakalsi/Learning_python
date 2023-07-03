class Book:
    def __init__(self,title):
        self.title=title

class Newspaper:
    def __init__(self,name):
        self.name=name

b1=Book("Ram")
b2=Book("Tom")
n1=Newspaper("Times of India")
n2=Newspaper("The Tribune")
print(n1.name)

print(type(b1))
print(type(n1))

print(type(b1)==type(n1))
print(type(b1)==type(b2))

print("using isinstance fn")
print(isinstance(n1,Newspaper))
print(isinstance(b1,Newspaper))