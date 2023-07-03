#import math
#print(dir(math))
# print("*"*100)
# print(dir(__builtins__))

##To print a list of all Python keywords
# import keyword
# print(keyword.kwlist)

# ## to see help about any builtin fn
# print(help(abs))

# ##To see the version of python
# import sys
# print(sys.version)

#print(bool(1000))

# a=3
# b=3
# print(id(a),id(b))
# print(a is b)
# a=30
# print(isinstance(a,int))
# print(a is b)

## Strings
##split,partition,join
# s1="C:\\rasna\\kalsi\\is\\my\\name"
# print(s1)
# print("After s1.split")
# print(s1.split("\\"))
# print("After s1.partition")
# print(s1.partition("\\"))
# str1="Er. Rasna Kalsi is preparing for TCS interview"
# str2="-".join(str1)
# print("Original str ",str1)
# print("String afteR joining using -.join(str1)",str2)
# print(str1.split())

# s="Rasna"
# t="kalsi"
# print(s[:2])
# print(s[1:4])
# print(s[-2:])
# print(s[:-2])
# print(s+t)
# print(s.find("a"))
# s1="Rasna"
# s2=s1.replace("a","t")
# print(s1,s2)

#LIST COMPREHENSION
# wt=100
# msg="obese" if wt>85 else "Hefty" if wt>65 else "Trim"
# print(msg)

# a,b,c=10,0,30
# res1=a>0 and b and c
# print(res1)

# n=0
# print("After setting n as 0")
# while(n<10):
#     print("inside while loop")
#     if (n==2):
#         break
#     n+=1
# else:
#     print("n has become >10")

##LISTS
l1=["Rasna","Ruby","Ruhi","Jia"]
# print(l1)
# l2=[]+l1//deep copy
# l2=l1//shallow copy
# print(l1 is l2)
# print(l1)
# print(l2)
# l2[0]="Kalsi"
# print("After changing l2[0] to kalsi")
# print(f"l1={l1},\nl2={l2}")

# for name in l1:
#     print(name,sep=";")
# i=len(l1)
# print("Printing using while loop")
# while(i>0):
#     print(l1[i-1])
#     i-=1
# else:
#     print("Finished printing list using while loop")

# for index,name in enumerate(l1):
#     print(index,name)

# l2=[10,30,20,34,7]
# l2.sort()
# print(l2)

# l3=[10,3,4,1,20,16]
# sl3=sorted(l3)
# sl4=[reversed(l3)]
# print(type(sl3),sl3)
# print(type(sl4),sl4)
# print(list(sl4))

#to empy the list
# l3=[1,2,3,4,5]
# l2=l3
# print(id(l2),id(l3))
# print(l2 is l3)
# del(l3)
# print(id(l2))
# print(l2)

# l1=[10,20,30]
# l2=l1
# print(f"l1={l1},l2={l2}")
# #l1[:]=[]
# del(l2[1])
# print(f"l1={l1},l2={l2}")


#lIST COMPREHENSION

# import random
# listr=[ random.randint(10,100) for i in range(20)]
# print(listr)

# #generate square and cube of all numbers b/w 0 and 10
# listsc=[(n,n**2,n**3) for n in range(10)]
# print(listsc)
# print(type(listsc[0]))

# #convert a list of string numbers to list of integers
# listn=[int(n) for n in ["10","20","30","40"]]
# print(listn)
# print(type(listn[0]))

#generate a list of even numbers in range 10 to 30
# liste=[n for n in range(30) if n%2 ==0 ]
# print(liste)

# ## replace vowel in a string with !
# str1="Rasna and mehtaab are beautiful mom and daugther"
# str1_new=[ ch if ch not in "aeiou" else "!" for ch in str1]
# print(str1_new)
# print("".join(str1_new))

##Functions
##Scenario1: Redefining a function
# def func1():
#     print("Hello Rasna")
# func1()
# def func1():
#     print("Hello Ruby")
# func1()

##Scenario #2 : Nested functions

# def func1():
#     print("Reached func1")
#     def func2():
#         print("Inner avatar")
#     print("Outer avatar")
#     func2()

# func1()
# func2()
# print(type(func2))

#Scenario #3 Checking return statemet

# def func1(a,b,c):
#     if a==1:
#         return "a is 1"
#     else:
#         return a+b+c

# print(func1(1,2,3))
# print(func1(10,20,30))
# l1=[2,3,4]
# print(*l1)
# print(func1(*l1))

#Scenario #3.2 Return multiple values using list
# def func2(a,b,c):
#     sum=a+b+c
#     product=a*b*c
#     #return[sum,product]
#     #return sum,product,a,b,c #returns a tuple containing (sum,product,a,b,c)
    

# l=func2(10,100,100)
# print(type(l))
# print(l)

# Scenario 4: Positional versus keyword arguments

##Positional arguments
# def fun(i,j,k="Ruhi"):
#     print(i+j)
#     print(k.upper())

# fun(1,3,"rasna")
# fun(10,2)

##Positional arguments #2

# def print_it(*args):
#     print()
#     print(args)
#     print(type(args))
#     for val in args:
#         print(val, end=" ")
#     print("Exiting print_it fn \n")

# l=[10,20,30]
# print_it(l)
# print_it(*l)
# print_it(1,2,3)
# print_it(11,22,33,44,)

##Scenario: Keyword arguments
# def print_it(i,j,str):
#     print(i+j,"?".join(str))

# print_it(str="Rasna",j=3)
# print_it(str="Ruhi",j=34,i=12)

# Scenario: Using variable length keyword arguments

# def print_it(a=10,b=2,str="ruby"):
#     print(a,b,str)
#     print(a+b)
#     print(str.upper())


# #print_it(a=10,s="Rasna")
# dic1={"a":10,"b":20,"str":"Rasna"}

# print_it(**dic1)
# print_it(*dic1)
# # i=0
# # for elem in dic1:

#     print("\n{}:{}".format(elem,i))
#     i=i+1

# def print_it(name="Sanjay",marks=100):
#     print(name,marks)

# d={"name":"Rasna","marks":10}
# print_it(*d)
# print_it(**d)


##FUNCTIONAL PROGRAMMING

# def func():
#     print("Hello")

# def sum(x,y,f):
#     print(x+y)
#     print(type(f))
#     f()

#f=func
# print(type(f))
# f()

# g=sum  #assignment of a function to a variable
# g(10,2,func)

#Lambda function
# print((lambda n: n*n*n)(3))
# print((lambda x,y,z:(x+y+z))(2,3,4))
# s="    Rasna kalsi is revising python       "
# print(s.strip())
# print(s.strip().upper())
# print("".join(s.split()))

##Assinging lambda fn to the variable and then invoking them.
# p=lambda n: n*n*n
# q=lambda x,y,z:(x+y+z)/3
# r=lambda s:s.lstrip().rstrip().upper()
# print(p(3))
# print(q(1,2,3))
# print(r("                         Rasna                         ")+"kalsi")

#Container types can also be passed to the lambda function

# lst1=[10,20,30,40,50]
# print((lambda l:sum(l))(lst1))

##Using map fn :
def func(n):
    return n*n

def even_filter(n):
    if n %2 ==0:
        return True

def cal_sum(x,y):
    print(x,y)
    return x+y


lst=[1,2,3,4,5]
# m1=map(func,lst)
# print(type(m1))
# print(list(m1))
# print(m1)
# f1=filter(even_filter,lst)
# print(list(f1))
from functools import reduce
s=reduce(cal_sum,lst)