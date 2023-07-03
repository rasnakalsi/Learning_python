class E:
    def __init__(self):
        self.type="Good"

class Book:
    def __init__(self,title,price,author=None):
        self.title=title
        self.price=price
        self.author=author
        self.chapters=[]

    def addchapter(self,chapter):
        self.chapters.append(chapter)

    def getbookpagecount(self):
        result=0
        for ch in self.chapters:
            result+=ch.pagecount
        return result

class Chapter:
    def __init__(self,name,pagecount):
        self.name=name
        self.pagecount=pagecount

class Author:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def __str__(self):
        
        return f"{self.fname} {self.lname}"


auth=Author("Leo","Tolstoy")
print(auth)
b1=Book("War and Peace",40.21,auth)
b1.addchapter(Chapter("Lesson1 ",200))
b1.addchapter(Chapter("Lesson2",300))
b1.addchapter(Chapter("Lesson3",400))
print(b1.author)
print(b1.getbookpagecount())
