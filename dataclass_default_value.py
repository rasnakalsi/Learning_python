# from dataclasses import dataclass
# @dataclass
# class Book:
#     title:str="No Title"
#     author:str="No Author"
#     pages:int=0
#     price:float=0.0


# b1=Book()
# print(b1)


##CASE 2: using field fn to specify default value

# from dataclasses import field,dataclass
# @dataclass
# class Book:
#     title:str="No Title"
#     author:str="No Author"
#     pages:int=0
#     price:float=field(default=10.00)


# b1=Book()
# print(b1)

##CASE 3: using default_factory 
# and specifying the fn to provide default value

from dataclasses import field,dataclass
import random

def price_func():
    return float(random.randrange(20,40))



@dataclass
class Book:
    title:str="No Title"
    author:str="No Author"
    pages:int=0
    price:float=field(default_factory=price_func)


b1=Book()
print(b1)

b2=Book()
print(b2)

