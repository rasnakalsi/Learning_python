class Book:
    def __init__(self,title,author,price):
        super().__init__()
        self.title=title
        self.author=author
        print("Value of price {price} and type of price : ",type(price))
        self.price=price
        
        self.discount=0.1

    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price} "

    def __getattribute__(self,name):
        if name=="price":
            p=super().__getattribute__("price")
            d=super().__getattribute__("discount")
            return p-(p*d)

        return super().__getattribute__(name)
    
    def __setattr__(self,name,value):
        print(name,value)
        if name=="price":
            if type(name) is not float:
                raise ValueError("The price attr is not a float")
        return super().__setattr__(name,value)


    
b1=Book("War and Peace","Leo Tolstoy",40.21)
b2=Book("The Catcher in the Rye","JD Salinger",100.31)
print(b1)

b1.price=float(40)
b2.price=43.32

