# x=open('file', 'w+')
# print(x.read())
# #x.seek(0)
# x.write(x.name)
# x.seek(0)
# print(x.read())
# print(x.name)    

# v = [1, 2, 3]
# def g(a,b,m):
#     return m(a,b)
  
# print(g(1, 1, lambda x,y: v[ x:y+1 ]))
# print(__name__)

# w = bool(23)
# x = bool('')
# y = bool(' ')
# z = bool([False])
# print(w,x,y,z)
# print([False])
# print(False)
# print(True)
# print(int(False))
# class Team:
#     def __init__(self):
#         print("Hello Ruhi!!")
#     def show_ID(self):
#         print(self.get_ID())
 
#     def get_ID(self):
#         return "anonymous"
 
 
# class A(Team):
#     # def __init__(self):
#     #     #Team.__init__(self)
#     #     print("Hi Rasna")
#     def get_ID(self):
#         return "Alpha"
#     def set_ID(self):
#         pass
#     def show_ID(self):
#         print("Its subclass show")
# a = A()
# a.show_ID()

# try:
#     file = open('file.txt', 'r')
#     # insert your code here
#     data=file.read()
#     file.seek(0)
#     rl_list=file.readlines()
#     print(type(data))
#     print(data)
#     #print("*"**90)
#     print(type(rl_list))
#     print(rl_list)
# except:
#     print('Something went wrong!')

# from p.m import f
# f()
# import p.m
# p.m.f()
# # import p.m.f
# # f()
# import p
# m.f()

# class A:
#     def __init__(self, x):
#         self.__a = x + 1
#         #print(__a)
 
 
# a = A(0)
# print(a.__a)

# x = lambda a, b: a ** b
# print(x(2, 10))
 
# class A:
#     def __init__(self, x=0):
#         self.x = x
 
#     def func(self):
#         self.x += 1
 
 
# class B(A):
#     def __init__(self, y=0):
#         A.__init__(self, 3)
#         self.y = y
 
#     def func(self):
#         self.y += 1
 
 
# b = B()
# b.func()
# print(b.x, b.y)

# import math
# print(math.e)
# result = math.e != math.pow(2, 4)
# print(int(result))
# print(math.pow(2,4))
# print(math.e != math.exp(2))

# x = 2
# y = 1
# x *= y + 1
# print(x)
# class Content:
#     title = "None"
 
#     def __init__(self, this):
#         self.name = this + " than " + Content.title
 
# text_1 = Content("Paper")
# text_2 = Content("Article")
# print(text_1.title)
# print(text_1.title == text_2.name)

# Content.title="Rasna"
# print(text_1.title)
# text_3=Content("Ruhi")
# print(text_3.name)

#from curses.ascii import isalnum
#import platform
# print(platform.version())
# print(platform.system())
# print(platform.processor())
# print(platform.architecture())
# print(platform.uname())
# print(platform.python_implementation())
# print(platform.python_version_tuple())

#num = 1
 
 
# def func():
#     num = num + 3
#     print(num)
 
 
# func()
 
# print(num)

# x = input()
# y = input()
# print(x + y)

# print(list('hello'))
# print(3 % 5)
# x = True
# y = False
# z = False
 
# if not x or y:
#     print(1)
# elif not x or not y and z:
#     print(2)
# elif not x or y or not y and x:
#     print(3)
# else:
#     print(4)

# x = 1
# y = 2
# z = x
# x = y
# y = z
# print(x, y)

# class Cat:
#     Species = 1
 
#     def get_species(self):
#         return 'kitty'
 
 
# class Tiger(Cat):
#     def get_species(self):
#         return
 
#     def set_species(self):
#         pass
 
 
# creature = Tiger()
# # print(hasattr(creature, "get_species"),
# #       hasattr(Cat, "set_species"))
# print(creature.get_species())
# print(Null==None)

# def func():
#     try:
#         print(23)
#     finally:
#         print(42)
 
 
# func()

# def func(text, num):
#     while num > 0:
#         print(text)
#     num = num - 1
 
 
# func('Hello', 3)

# z = 3
# y = 7
# x = y < z and z > y or y > z and z < y
# print(x)

# ka

# try:
#     first_prompt = input("Enter the first value: ")
#     a = len(first_prompt)
#     second_prompt = input("Enter the second value: ")
#     b = len(second_prompt) * 2
#     print(a/b)
# except ZeroDivisionError:
#     print("Do not divide by zero!")
# except ValueError:
#     print("Wrong value.")
# except:
#     print("Error.Error.Error.")

# for i in range(1,6):
#     print(str(i)*5)

# for i in range(1,6):
#     print(i,i,i,i,i,sep="")

# foo = [i + i for i in range(5)]
# print(foo)
#print("Rasna21@".isalnum())
# print(sorted("321"))

# print("".join(sorted("321")))

# tmp=list("321")
# print(tmp)
# tmp.sort()
# print(tmp)
# print("".join(tmp))

# d = {}
# d[1] = 1
# d['1'] = 2
# d[1] += 1
 
# sum = 0
 
# for k in d:
      #print(k)
#     sum += d[k]
 
# print(sum)

# tmp="321".sort()
# print(tmp)
# print(str(tmp))

# l=[9,1,34,49,1,9,7,9,32]
# print(l.pop())
# print(l.pop(0))
# print(l.count(9))
# print(l.index(34))


# i = 4
# while i > 0:
#     i -= 2
#     print('*')
#     if i == 2:
#         break
# else:
 
#     print('*')

# plane = "Cessna"
# counter = 0
# str=plane*2
# print(str)
# for c in plane * 2:
#     if c in ["e", "a"]:
#         counter += 1
# print(counter)

# def func(p1, p2):
#     p1 = 1
#     p2[0] = 42
 
 
# x = 3
# y = [1, 2, 3]
 
# func(x, y)
 
# print(x, y[0])
# class A:
#     def __init__(self, name):
#         self.name = name
 
 
# a = A('class')
 
# print(a)
# num = '7' * '7'
# print(num)

# def func(x):
#     return 1 if x % 2 != 0 else 2
 
 
# print(func(func(1)))

# def func(num):
#     res = '*'
#     for _ in range(num):
#         res += res
#     return res
 
 
# for x in func(2):
#     print(x, end='')


# data = ['Peter', 404, 3.03, 'Wellert', 33.3]
# print(data[1:3])
# in=10
# print(in)

# class A:
#     def __init__(self):
#         self.i = 0
#         self.calc(10)
#         print('i from A is', self.i)
 
#     def calc(self, i):
#         self.i = 2 * i
 
 
# class B(A):
#     def __init__(self):
#         super().__init__()
 
#     def calc(self, i):
#         self.i = 3 * i
# b = B()
# def func(x):
#     try:
#         x = x / x
#     except:
#         print('a', end='')
#     else:
#         print('b', end='')
#     finally:
#         print('c', end='')
 
 
# func(1)
# func(0)
# x = 1
# y = 2
# x, y, z = x, x, y
# z, y, z = x, y, z
# print(x, y, z)

# def check(i):
#      print("Have a look at Python Bitwise Operator")
#      return i

# print(500>20>check(50))
# a=10
# b=20
# c=40
# d=50

# value = a + b * c - d
# print(value)

# z = y = x = 1
# print(x, y, z, sep='*')

# try:
#     print(5/0)
#     break
# except:
#     print("Sorry, something went wrong...")
# except (ValueError, ZeroDivisionError):
#     print("Too bad...")

# from datetime import datetime
 
# datetime = datetime(2019, 11, 27, 11, 27, 22)
# print(datetime.strftime('%Y/%b/%d %H:%M:%S'))

# class Test:
#     def __init__(self, s='Welcome'):
#         self.s = s
 
#     def print(self):
#         print(self.s)
 
 
# x = Test()
# x.print()
# i=0
# def print(name):
#     j=0
#     if j==0:
#        i=0
#     else:
#         i+=1
#     j=1

#     if i==10:
#         return
#     print("Hello Rasna!!")

# class Economy:
#     def __init__(self):
#         self.econ_attr = True
 
 
# class Business(Economy):
#     def __init__(self):
#         super().__init__()
#         self.busn_attr = False
 
 
# econ_a = Economy()
# econ_b = Economy()
# busn_a = Business()
# busn_b = Business()

# print(busn_b is busn_a)
# print(busn_a)
# print(busn_b)

# busn_b=busn_a
# print(isinstance(busn_a, Economy)
#       and isinstance(econ_a, Business), end=" ")
# print(busn_b is busn_a or econ_a is econ_b)

# print(econ_a is econ_b)
# print(busn_a)
# print(busn_b)
###print("Rasaaana")

# class Test:
#     #id=0
#     def __init__(self, id):
#         self.id = id
#         id = 100
 
 
# x = Test(23)
 
# print(x.id)
# print(Test.id)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a[::2])

# i = 0
# while i <= 3:
#     i += 2
#     print('*')


#print(10<"1"+'0')

# nums = [3, 4, 5, 20, 5, 25, 1, 3]
# nums.pop(1)
# print(nums)
# x = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
 
# def func(data):
#     res = data[0][0]
#     for da in data:
#         for d in da:
#             if res < d:
#                 res = d
#     return res
 
# print(func(x[0]))
# print("King's cross station")
# print("All the king's horses")
# print("The knights who say 'NI!!'")
# L = [i for i in range(-1, -2,-1)]
# print(L)

# for i in range(-1,2):
#     print(i)
# import os
# os.mkdir(".\\temp2")
# l1=[1,12,3]
# l2=[4,5,6]
# x=map(lambda x,y:True,l1,l2)
# print(list(x))
# z=map(lambda a,b: a if a>b else b,l1,l2)
# print(list(z))

# x = [0, 1, 2]
# print(x)
# x.insert(0, 1)
# print(x)
# del x[1]
# print(x)
# print(sum(x))


# class A:
#     pass
 
 
# class B(A):
#     pass
 
 
# class C(B):
#     pass
 
 
# print(issubclass(C, A))

# x = 1
# def a(x):
#     return 2 * x
 
 
# x = 2 + a(x)      # Line 8
# print(a(x))       # Line 9

# list1 = [1, 3]
# list2 = list1
# list1[0] = 4
# print(list2)

# file = open('data.txt', 'w+')
# print(type(file))
# print('Name of the file: ', file.name)
 
# s = 'Peter Wellert\nHello everybody'
# file.write(s)
# file.seek(0)
# print(file.read(8))
# print(file.read(8))
# file.seek(0)
# str=file.read()
# print(str)
# for line in file.read(8):
#     print(line)
 
# file.close()

# class Storage:
#     def __init__(self):
#         self.rack = 1

#     def get(self):
#         return self.rack 
#     # Insert a method here
 
 
# stuff = Storage()
# print(stuff.get())

# x = '\''
# print(len(x))

# x = 1 // 5 + 1 / 5

# print(x)

# import platform
# print(platform.platform())
# x = 1 / 2 + 3 // 3 + 4 ** 2

# print(x)

# class Student():
#       __SchoolName="DAV"
#       def __init__(self,name,age):
#             print("Inside student init fn")
#             self._name=name
#             self._age=age
      
#       def _student_details(self):
#          print(self._name+", "+str(self._age))


# class eng_student(Student):
#       def __init__(self,name,age):
#             super().__init__(name,age)
#             print("inside eng_student init fn")
# #            print(Student.__SchoolName)
#             self.name=name
#             self.age=age
#             super()._student_details()

# s1=Student("Rasna",44)
# print(s1._Student__SchoolName)
# s1._name="Ruhi"
# print(s1._name)
# print(s1._age)
# #s1.__student_details()
# es1=eng_student("Er Rasna",44)
# print(es1.name,es1.age)

# x = 0
# while x < 6:
#     x += 1
#     if x % 2 == 0:
#         continue
#     print('*')

# strng = "John,Doe,42"
# strng = "".join(strng.split(","))
# print(strng[-2])
# print(strng)

# foo = (1, 2, 3)
# print(foo.index(0))

# class A:
 
#     A = 7
 
#     def __init__(self):
#         self.a = 0
 
 
# print(hasattr(A, 'A'))

# plane = "Blackbird"
# counter = 0
# for c in plane + 2:
#     if c in ["1", "2"]:
#         counter += 1
# print(counter)

# class Test:
#     def __init__(self, x=0):
#         self.x = x
# obj=Test("1")

# colors = ['red\n', 'yellow\n', 'blue\n']
# file = open('wellert.txt', 'w+')
# file.writelines(colors)
# #file.close()
# file.seek(0)
# for line in file:
#     print(line)

# data = [1, 2, 3, 4, 5, 6]
 
# for i in range(1, 6):
#     data[i - 1] = data[i]
 
# for i in range(0, 6):
#     print(data[i], end=' ')

# data = set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
# print(len(data))
# print(data)

# try:
#     raise BaseException
# except Exception:
#     print("c")
# except BaseException:
#     print("a")
# except:
#     print("b")



# x, y = 3.0, 0.0
# try:
#     z = x / y
# except ArithmeticError:
#     z = -1
# else:
#     z = -2
# print(z)

# import os
 
# os.mkdir('thumbnails')
# os.chdir('thumbnails')
 
# sizes = ['small', 'medium', 'large']
 
# for size in sizes:
#     os.mkdir(size)
 
# print(os.listdir())

#print(1 // 2 * 3)
# def increment(c, num):
#     c.count += 1
#     num += 1
 
 
# class Counter:
#     def __init__(self):
#         self.count = 0
 
 
# counter = Counter()
# number = 0
 
# for i in range(0, 100):
#     increment(counter, number)
 
# print(
#     "counter is "
#     + str(counter.count)
#     + ", number of times is "
#     + str(number)
# )

# data = [[0, 1, 2, 3] for i in range(2)]
# print(data[2][0])


#print(1 * 1)
# import calendar
# print(calendar.weekheader(2))

# data = 'abcdefg'
 
 
# def func(text):
#     del text[2]
#     return text
 
 
# print(func(data))

# class Test:
#     def __init__(self, s):
#         self.s = s
 
#     def print(self):
#         print(self.s)
 
 
# x = Test('Hello Python')
# x.print()

# class Aircraft:
#     def start(self):
#         return "default"
 
#     def take_off(self):
#         self.start()
 
 
# class FixedWing(Aircraft):
#     pass
 
 
# class RotorCraft(Aircraft):
#     def start(self):
#         return "spin"
 
 
# fleet = [FixedWing(), RotorCraft()]
# for airship in fleet:
#     print(airship.start(), end=" ")

# b = bytearray(3)
# print(b)

# class Control:
#     my_ID = 1
 
#     def say(self):
#         return self.my_ID
 
 
# class Button(Control):
#     my_ID = 2
 
 
# class Radio(Button):
#     def say(self):
#         return -self.my_ID
 
 
# selection = Radio()
# element = Control()
# start = Button()
# print(isinstance(start,Button))
# start.my_ID=-2

# data = {'1': '0', '0': '1'}
 
# for d in data.vals():
#     print(d, end=' ')

# with open('data.txt', 'w') as f:
#     f.write("I'm gonna make him an offer he can't refuse.")
 
# with open('data.txt', 'r') as f:
#     data = f.readlines()
#     print(data)
#     for line in data:
#         words = line.split()
#         print(words)


# import random
# data = [10, 20, 30]
# random.shuffle(data)
# print(data)

# def f(a,b):
#     return a(b)
 
 
# print(f(lambda x: x and True, 1 > 0))


# try:
#     f = open("non_existing_file", "w")
#     print(1, end=" ")
#     s = f.readline()
#     print(2, end=" ")
# except IOError as error:
#     print(3, end=" ")
# else:
#     f.close()
#     print(4, end=" ")

# data = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
# for i in range(0, 4):
#     print(data[i].pop(), end=' ')

# x= 1
# while x < 10:
#     print('*')
#     x = x << 1
# print("" in "alphabet")
# print("" not in "")
# print("xyz" not in "uvwxyz")

# class Storage:
#     def __init__(self):
#         self.rack = 1
 
#     def get(self):
#         return self.rack
 
#     def print(self):
#         # Insert a method here
#         print(get())
 
 
# stuff = Storage()
# print(stuff.print())

# plane = "Blackbird"
# counter = 0
# for c in plane + 2:
#     if c in ["1", "2"]:
#         counter += 1
# print(counter)

# x = """
# """
# print(len(x))
# print("rasna"+x+"kalsi")

# x = True
# y = False
# x = x or y
# y = x and y
# x = x or y
# print(x, y)

# x = 0
# while x < 6:
#     x += 1
#     if x % 2 == 0:
#         continue
#     print('*')

# x, y = 3.0, 1
# try:
#     z = x / y
# except ArithmeticError:
#     print("I am in except block")
#     z = -1
# else:
#     print("inside else block")
#     z = -2
# finally:
#     print("inside finally block")
#     z=-3
# print(z)

# z = 3
# y = 7
# x = y == z and y > z or z > y and z != y
# print(x)
# import sys
# colors = ['red\n', 'yellow\n', 'blue\n']
# file = open('wellert.txt', 'w+')
# file.writelines(colors)
# #file.close()
# file.seek(0)
# for line in file:
#     print(line)

# sys.exit()
# print("Rasna")


# class Aircraft:
#     def start(self):
#         return "default"
 
#     def take_off(self):
#         self.start()
 
 
# class FixedWing(Aircraft):
#     pass
 
 
# class RotorCraft(Aircraft):
#     def start(self):
#         return "spin"
 
 
# fleet = [FixedWing(), RotorCraft()]
# for airship in fleet:
#     print(airship.start(), end=" ")

# my_list = [0 for i in range(1, 3)]
# print(my_list)

from ast import BitAnd
from re import X


class A:
 
    def __init__(self, v=2):
        self.v = v
 
    def set(self, v=1):
        self.v += v
        return self.v
 
 
# a = A()
# b = a
# print(id(a))
# print(id(b))
# print(id(A))
# b.set()
 
#print(a.v)
# print('Peter' 'Wellert')

# data = {}
 
 
# def func(d, key, value):
#     d[key] = value
#     return d
 
 
# print(func(data, '1', 'Peter'))


#print(chr(ord('z') - 2))

# i = 0
# while i <= 5:
#     i += 1
#     if i % 2 == 0:
#         break
#     print('*')

# data = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
# for i in range(0, 4):
#     print(data[i].pop(), end=' ')

# num = 1
 
 
# def func():
#     num = 3
#     print(num, end=' ')
 
 
# func()
 
# print(num)

print("\\")
class A:
    def __init__(self, x=2, y=3):
        self.x = x
        self.y = y
 
    def __str__(self):
        print("inside str fn")
        return 'A'
 
    def __eq__(self, other):
        return self.x * self.y == other.x * other.y
 
 
# a = A(1, 2)
# b = A(2, 1)
# print(a)
# print(a == b)

# x = 8

# y = 10

# result = x // 3 * 3 / 2 + y % 2 ** 2

# print(result)

# for n in range(1, 6, 1):
#     print(str(n) * 5)

# x = int(input())
# y = int(input())
# x = x % y
# x = x % y
# y = y % x
# print(y)

# import pi from math
# print(pi)

# x = 1 + 1 // 2 + 1 / 2 + 2

# print(x)

# def f(a,b):
#     return a(b)
 
# print(f(lambda x: x and True, 1 > 0))

# def increment(c, num):
#     c.count += 1
#     num += 1
 
 
# class Counter:
#     def __init__(self):
#         self.count = 0
 
 
# counter = Counter()
# number = 0
 
# for i in range(0, 100):
#     increment(counter, number)
 
# print(
#     "counter is "
#     + str(counter.count)
#     + ", number of times is "
#     + str(number)
# )


# def func(message, num=1):
#     print(message * num)
 
 
# func('Hello')
# func('Welcome', 3)

# b = bytearray(3)
# print(b)
# data = [4, 2, 13, 7, 11,1,0,-2,-1]
# res = data[0]
 
# for d in data:
#     if d < res:
#         res = d
 
# print(res)

# try:
#     raise Exception(1, 2, 3)
# except Exception as e:
#     print(len(e.args))

# a = [1, 2, 3, 4, 5]
# print(a[3:0:-1])

# data = set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
# print(len(data))

# data = 'abbabadaadbbaccabc'
# print(data.count('ab', 1))

# x = '\\\\'
# print(len(x))

#print(float('1.3'))
# print(1 / 1)
# class Control:
#     my_ID = 1
 
#     def say(self):
#         print("inside control say fn")
#         return self.my_ID
 
 
# class Button(Control):

#     my_ID = 2
 
 
# class Radio(Button):
#     def say(self):
#         print("inside radio--say fn")
#         return -self.my_ID
 
 
# selection = Radio()
# element = Control()
# start = Button()
# print(start.my_ID==-2)
# print(selection.my_ID==2)
# print(isinstance(start,Button))
# print(selection is Radio())
# print(start is element)

# class Test:
#     def __init__(self, s):
#         self.s = s
 
#     def print(self):
#         print(s)
 
 
# x = Test('Hello Python')
# x.print()

# try:
#     print('try')
# except:
#     print('except')
# finally:
#     print('finally')

# x = 1
# x = x == x
# print(x)

# people = {}
 
 
# def add_person(index):
#     if index in people:
#         people[index] += 1
#     else:
#         people[index] = 1
 
 
# add_person('Peter')
# add_person('Paul')
# add_person('peter')
 
# print(len(people))
# print(people)

# pairs = [[2, 1], [-1, -1]]
# new_pairs = map(lambda p: sorted(p), pairs)
# print(list(new_pairs)[0][0])

# header = 2 * '+-' + '+'
# plus = 0
# for x in header:
#     if x not in header:
#         plus += 1
# print(plus)

# data = ['Peter', 'Paul', 'Mary', 'Jane']
# print("\n".join(data))

# w = [7, 3, 23, 42]
# x = w[1:]
# y = w[1:]
# z = w
# y[0] = 10
# z[1] = 20
# print(w)

# from random import randint
 
# for i in range(2):
#     print(randint(1, 2), end='')

# class A:
#     def __init__(self, x=0):
#         self.x = x
 
 
# obj1 = A(2)
# obj2 = A(2)
# print(id(obj1) == id(obj2))
 
# str1 = 'Hello'
# str2 = 'Hello'
# print(id(str1) == id(str2))

# value = input("Enter a value: ")
# print(10/value)

# x = 16
# while x > 0:

#     print('*')

#     x //= 2

# x = float(input())
# y = float(input())
# print(y ** (1 / x))

# source = [1, 2, 4, 8, 16]
# target = [x // 2 for x in source if x < 10]
# print(target[1])
# x=[range(0,2)]
# print(x)
# print(len([i for i in range(0, -2)]))

# x = 0
# y = 1
# x = x ^ y
# y = x ^ y
# y = x ^ y
# print(x, y)

#print(type(1J))

# data = [[x for x in range(y)] for y in range(3)]
# print(data)
 
# for d in data:
#     if len(d) < 2:
#         print('*')


# def boolean(op):
#     return op(False, True)
 
 
# print(boolean(lambda x,y: x if x else y))

# data = [i for i in range(-1, 2)]
# print(data)

# data = (1,) * 3
# print(data)
# data[0] = 2
# print(data)

# data = {'a': 1, 'b': 2, 'c': 3}
# print(data['a'])

# data = [1, {}, (2,), (), {3}, [4, 5]]
# points = 0
 
# for i in range(len(data)):
#     if type(data[i]) == list:
#         points += 1
#     elif type(data[i]) == tuple:
#         points += 10
#     elif type(data[i]) == set:
#         print(i)
#         points += 100
#     elif type(data[i]) == dict:
#         points += 1000
#     else:
#         points += 10000
 
# print(points)

# numbers = (1, 2, 5, 9, 15)
 
 
# def filter_numbers(num):
#     nums = (1, 5, 17)
#     if num in nums:
#         return True
#     else:
#         return False
 
 
# filtered_numbers = filter(filter_numbers, numbers)
# for n in filtered_numbers:
#     print(n)


# fruits1 = ['Apple', 'Pear', 'Banana']
# fruits2 = fruits1
# fruits3 = fruits1[:]
 
# fruits2[0] = 'Cherry'
# fruits3[1] = 'Orange'
 
# res = 0
 
# for i in (fruits1, fruits2, fruits3):
#     if i[0] == 'Cherry':
#         res += 1
#     if i[1] == 'Orange':
#         res += 10
 
# print(res)

# data = ()
# print(data.__len__())

# def func(x):
#     global y
#     y = x * x
#     return y
 
 
# func(2)
# print(y)

# class A:
#     def __init__(self, x=1):
#         self.x = x
 
 
# class B(A):
#     def __init__(self, y=2):
#         super().__init__()
#         self.y = y
 
 
# b = B()
# print(b.x, b.y)


# data = [(0, 1), (1, 2), (2, 3)]
# res = sum(i for j, i in data)
# print(res)

# x = True
# y = False
# z = False
 
# if x or y and z:
#     print('TRUE')
# else:
#     print('FALSE')


def attic(x):
    assert x != 0
    return 1 / x
 
 
# def floor(x):
#     try:
#         attic(x)
#     except:
#         raise
 
 
# try:
#     x = attic(0)
# except RuntimeError:
#     x = -3
# except:
#     print("inside except block")
#     x = -2
# else:
#     x = -1
# print(x)

# def test(x, y=23, z=10):
#     print('x is', x, 'and y is', y, 'and z is', z)
 
 
# test(3, 7)
# test(42, z=24)
# test(z=60, x=100)

# def func(item):
#     item += [1]
 
 
# data = [1, 2, 3, 4]
# func(data)
# print(len(data))

# x, y = 0.0, 3.0
# try:
#     z = x / y
# except ArithmeticError:
#     z = -1
# else:
#     z = -2
# print(z)

# def test(x=1, y=2):
#     x = x + y
#     y += 1
#     print(x, y)
 
 
# test()

# class A:
#     def __init__(self):
#         self.i = 1
 
#     def func(self):
#         self.i = 10
 
 
# class B(A):
#     def func(self):
#         self.i += 1
#         return self.i
 

# try:
#     if '1' != 1:
#         raise FirstError
#     else:
#         print('FirstError has not occured.')
# except FirstError:
#     print('FirstError has occured.')
# else:
#     print('None of the above.')

 
# b = B()
# print(BitAnd.func())


# class A:
#     def __init__(self):
#         self.calc(10)
 
#     def calc(self, i):
#         self.i = 3 * i
 
 
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print('i from B is', self.i)
 
#     def calc(self, i):
#         self.i = 2 * i
 
 
# b = B()

# try:
#     file = open('data.txt', 'r')
#     file.write('Hello file!')
# except:
#     print('An error occurred.')
# else:
#     print('The content is written successfully.')

# my_list = [[3-i for i in range(3)] for j in range(3)]
# result = 0
 
# for i in range(3):
#     result += my_list[i][i]
 
# print(result)


# nums = [1, 2, 3]
# print(nums[::-1])
# data = ('Peter',) * (len(nums) - nums[::-1][0])
# print(data)

# a = 1
# b = 0
# c = a & b
# d = a | b
# e = a ^ b
# print(c + d + e)

# foo = "Mary had 21 little sheep"
# print(foo.split()[2].isdigit())

# data1 = 'a', 'b'
# data2 = ('a', 'b')
# print(data1,type(data1))
# print(data2,t1700ype(data2))
# print(data1 == data2)

# order = int(input('Please enter the order value: '))
# state = input('Please enter the state (as postal abbreviation): ')
# delivery = 0
 
# if state in ['NC', 'SC', 'VA']:
#     if order <= 1000:
#         delivery = 70
#     elif 1000 < order < 2000:
#         delivery = 80
#     else:
#         delivery = 90
# else:
#     delivery = 50
# if state in ['GA', 'WV', 'FL']:
#     if order > 1000:
#         delivery += 30
#     if order < 2000 and state in ['WV', 'FL']:
#         delivery += 40
#     else:
#         delivery += 25
# print(delivery)

# class A:
#     def __str__(self):
#         return 'A'
 
 
# class B(A):
#     def __str__(self):
#         return 'B'
 
 
# class C(B):
#     def __str__(self):
#         return 'C'
 
 
# b = B()
# a = A()
# c = C()
# print(c, b, a)

#print(3 * (1 + 2) ** 2 - (2 ** 2) * 3)

# import sys
# print(sys.path)

# import os
# print(os.environ.get("PYTHONPATH"))

# list1 = ['Peter', 'Paul', 'Mary', 'Jane']
# list2 = ['Peter', 'Paul', 'Mary', 'Jane']
 
# print(list1 is not list2)
# print(list1 != list2)
 
# list1 = list2
 
# print(list1 is not list2)
# print(list1 != list2)


class A:
 
    A = 1
 
    def __init__(self, x=2):
        self.x = x + A.A
        A.A += 1
 
    def set(self, x):
        self.x += x
        A.A += 1
 
 
# a = A()
# a.set(2)
# print(a.x)
# print(A.A)
# print(hasattr(A,"A"))

# w = 7
# x = 3
# y = 4
# z = True
# a = w + x * y
# b = w + x / z
 
# if a>b:
#     print('TRUE')
# else:
#     print('FALSE')

# print(a,b)

# num=input("please enter a number")
# print(int(num)+1)

# s="rhyme"
# print(s[-3:-5])
# print("rhy" in s)
# print(s+"rasna")
# print(s*2)
# print(s-2)
# file = open('data.txt', 'r+')
# txt = "I'm gonna make him an offer he can't refuse.i am going to canada\n getting ready"
# file.writelines(txt)
# file.seek(0)
# lines = file.readlines()
# print(lines)
# for line in lines:
#     print(line)
# file.close()

# class Example:
#     def __str__(self):
#         return __name__
 
 
# thing = Example()
# print(thing)

# x = (1, 4, 7, 9, 10, 11)
# y = {2: 'A', 4: 'B', 6: 'C', 8: 'D', 10: 'E', 12: 'F'}
# res = 1
# for z in x:
#     if z in y:
#         res += z
# print(res)

# for z in y:
#     print(z)

# print(ord("m"))
# print('miKE' > 'miKe')
# print()

# data = [[42, 17, 23, 13], [11, 9, 3, 7]]
# res = data[0][0]
# for da in data:
#     for d in da:
#         if res > d:
#             res = d
# print(res)

# class A:
#     def __str__(self):
#         return 'A'
 
 
# class B(A):
#     def __str__(self):
#         return 'B'
 
 
# class C(B,A):
#     pass
 
 
# c = C()
# print(c)
# print(C.__bases__)

# vect = ["alpha", "bravo", "charlie"]
# new_vect = map(lambda s: s[0].upper(), vect)
# print(list(new_vect)[1])


# s = 'three'
# e = 0
# try:
#     e = int(s)
# except ArithmeticError:
#     e = 1
# except:
#     print("inside except block")
#     e = 2
# else:
#     e = 3
# print(e)

# print( not 'a' in 'abc')
# print('123' in '1-2-3')
# print('\n' in """
# """)
# print(not('a' not in 'abc'))

# def fun(n):
#     s = '+'
#     for i in range(n):
#         s += s
#         yield s
 
 
# for x in fun(2):
#     print(x, end='')


# def o(p):
#     def q():
#         return '*' * p
#     return q
 
 
# r = o(1)
# s = o(2)
# print(r() + s())



# try:
#     print('try')
#     print(10 / 0)
# except:
#     print('except')
# else:
#     print('else')
# finally:
#     print('finally')

# data = 'Hello@Peter!!'
# print(data.lower())

# def get_names():
#     names = ['Peter', 'Paul', 'Mary', 'Jane', 'Steve']
#     return names[2:]
 
 
# def update_names(names):
#     res = []
#     for name in names:
#         res.append(name[:3].upper())
#     return res
 
 
# print(update_names(get_names()))

# x = [0, 1, 2]
# print(x)
# x[0], x[2] = x[2], x[0]
# print(x)

# print((+1E10))
# print(type(5.0))
# print(type('True'))
# print(type(False))

# def quote(quo):
 
#     def embed(str):
#         return quo + str + quo
 
#     return embed
 
 
# dblq = quote('"')
# print(dblq('Jane Doe'))

# print('"Rasna"')
# str="Rasna"
# quo="'"
# print(quo+str+quo)
# print(str)

# x = int(input())
# y = int(input())
# x = x % y
# x = x % y
# y = y % x
# print(y)

# points = 0
# try:
#     file = open('peoples.txt', 'r')
#     data = file.readlines()
#     for d in data:
#         points += float(d.split(':')[1])
#     file.close()
#     print(points)
# except:
#     print('The file could not be opened!')

# l = [x for x in range(1, 10, 3) if x % 2 == 0]
# print(len(l))
# print(l)
# print(list(range(1,10,3)))

# def func1(a):
#     return a ** a
 
 
# def func2(a):
#     return func1(a) * func1(a)
 
 
# print(func2(2))

# data=["Peter","Paul","Mary","Jane"]
# da=data[1:]
# for d in data:
#     d
#     if len(d)==4:
#         print(d)


# class A:
 
#     A = 23
 
#     def __init__(self):
#         self.a = 42
 
# obj=A()
# print(hasattr(obj, 'a'))

# data = [1, 2, 3, 4]
# data = list(map(lambda x: x*2, data))
# print(data)

# try:
#     raise Exception
# except BaseException:
#     print('1')
# except Exception:
#     print('2')
# except:
#     print('3')



#print(chr(ord('p') + 3))

# print(not 0)
# print(not 23)
# print(not '')
# print(not 'Peter')
# print(not None)

# s = lambda x: 0 if x == 0 else 1 if x > 0 else -1
 
# print(s(-273.15))

# class A:
#     __A=1
#     def __init__(self):
#         pass
        
 
 
# a = A()
# print(hasattr(a, 'A'))


# def func1(x):
#     return str(x)
 
 
# def func2(x):
#     return str(2 * x)
 
 
# print(func1(1) + func2(2))

# class Failure(Exception):
#     def __init__(self, message):
#         print("inside init fn")
#         self.message = message
#         print(self.message)
 
#     def __str__(self):
#         print(self.message)
#         return "out of order"
 
 
# try:
#     print("turn on")
#     raise Failure("crash")
# except Failure as problem:
#     print(problem)
# else:
#     print("success")

# 1
# room = input('Enter the room number: ')
# rooms = {101: 'Gathering Place', 102: 'Meeting Room'}
# if not room in rooms:
#     print('The room doesn\'t exist.')
# else:
#     print('The room name is: ' + rooms[room])


# my_tuple = (0, 1, 2, 3, 4, 5, 6)
# foo=list(filter(lambda x: x-0 and x-1,my_tuple))
# print(foo)

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(x[::2])
# x[::2] = 10, 20, 30, 40, 50
# print(x)
# x = float('23.42')
# print(int(x)+False)
# print(str(x))
# print(bool(x)+True)
# print(bool(x))

from datetime import date
 
# date_1 = date(1992, 1, 16)
# date_2 = date(1991, 2, 5)
 
# print(date_1 - date_2)

# try:
#     value = input("Enter a value: ")
#     print(int(value)/int(value))
# except ValueError:
#     print("Bad input...")
# except ZeroDivisionError:
#     print("Very bad input...")
# except TypeError:
#     print("Very very bad input...")
# except:
#     print("Booo!")

# data = {'z': 23, 'x': 7, 'y': 42}
 
# for _ in sorted(data):
#     print(data[_], end=' ')


# def func1(param):
#     return param
 
 
# def func2(param):
#     return param * 2
 
 
# def func3(param):
#     return param + 3
 
 
# print(func1(func2(func3(1))))


# data = {}
# data[1] = 1
# data['1'] = 2
# data[1.0] = 4
# print(data) 
# res = 0
# for d in data:
#     res += data[d]
 
# print(res)


# import math
 
# x = -1.5
# print(abs(math.floor(x) + math.ceil(x)))


# num = 42
 
# Code-1
# if num % 2 == 0:
#     even = True
# else:
#     even = False

# print(even)
# # Code-2
# even = True if num % 2 == 0 else False
# print(even)
 
# # Code-3
# even = num % 2 == 0
# print(even)

# class A:
#     def __init__(self):
#         self.text = 'abc'
#         self.count = 0
 
#     def __iter__(self):
#         print("inside iter fn\n")
#         return self
 
#     def __next__(self):
#         print("\ninside next fn")
#         if self.count == len(self.text):
#             raise StopIteration
#         value = self.text[self.count]
#         self.count += 1
#         return value
# for x in A():
#     print(x, end='')
 

# class A:
#     pass
 
 
# class B(A):
#     pass
 
 
# class C(B):
#     pass
 
 
# print(issubclass(A, C))


#print(1 // 2)
# print("new section")
# box = {}
# jars = {}
# crates = {}
 
# box['biscuit'] = 1
# box['cake'] = 3
 
# jars['jam'] = 4
 
# crates['box'] = box
# crates['jars'] = jars
 
# print(len(crates['box']))

 
# x = {(1, 2): 1, (2, 3): 2}
# print(x[1, 2])

# data = ['peter', 'paul', 'mary']
# for d in data:
#     data.append(d.upper())
# print(data)


# from sys import argv
# print(argv[1] + argv[2])

# for i in range(1):
#     print('*')
# else:
#     print('*')

# s="rhyme"
# print(s[::-2])
# try:
#     raise Exception
# except BaseException:
#     print('1', end='')
# else:
#     print('2', end='')
# finally:
#     print('3', end='')
# x = 2

# y = 6

# x += 2 ** 3

# x //= y // 2 // 3

# print(x)
# print("hi")
# print()
# print("hello")

# class Class1:
#     def m(self):
#         print("In Class1")
 
# class Class2(Class1):
#     def m(self):
#         print("In Class2")
#         super().m()
 
# class Class3(Class1):
#     def m(self):
#         print("In Class3")
#         super().m()
 
# class Class4(Class3, Class2):
#     def m(self):
#         print("In Class4")  
#         super().m()
      
# obj = Class4()
# obj.m()
# print(Class4.mro())

# class A:
#     x = 23
 
 
# class B(A):
#     x = 42
 
 
# class C(B):
#     pass
 
 
# obj = C()
# print(obj.x)
# print(C.mro())

# for i in range(1):
#     print('*')
# else:
#     print('*')

# list1 = [3, 7, 23, 42]
# list2 = [3, 7, 23, 42]
# print(list1 is list2)
# print(list1 == list2)

# data = ['Peter', 'Paul', 'Mary', 'Jane']
# res = 0
# for i in ("Peter","Steve","Jane"):
#     if i not in data:
#         res+=100

# print(res)

# x = 23 + 42
# y = '23' + '42'
# z = '23' * 7
# for i in (x,y,z):
#     print(type(i),sep=" ")

#print(2 ** 3 ** 2 ** 1)

# def fun(x):
#     assert x >= 0
#     return x ** 0.5
 
 
# def mid_level(x):
#     try:
#         fun(x)
#     except:
#         print("inside except block")
#         raise RuntimeError
 
 
# try:
#     x = mid_level(-1)
# except RuntimeError:
#     print("inside runtime error")
#     x = -1
# except:
#     x = -2
# print(x)
# print( chr(49)=="1")
# print("Al"*2<="Alan")
# print("9"*3<"9"*9)
# #print("9"*1<=1*2)
# print(ord("1"))

#print(Hello, World!)

# class A:
#     def a(self):
#         print('a')
 
# class B:
#     def a(self):
#         print('b')
 
# class C(B, A):
#     def c(self):
#         self.a()
 
# o = C()
# o.c()
# print(C.__bases__)
# print(C.mro())

# x = 1
# print(x)
# print(-x)
# print(++++x)

# class BluePrint:
#     __element = 1
 
#     def __init__(self):
#         self.component = 1
 
#     def __action(self):
#         print("inside __action fn")
        
 
 
# product = BluePrint()

# product._BluePrint__action()


import calendar
import math
 
# cal = calendar.isleap(2019)
# print(cal)
# num=math.ceil(float(input("How many do you need??")))
# print(num)

# x = '\\\\'
# print(len(x))


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# x = 0
# while x < 10:        # Line 3
#     print(nums(x))   # Line 4
#     if nums[x] == 7:  # Line 5
#         break        # Line 6
#     else:            # Line 7
#         x += 1       # Line 8


# data = ((1, 2),) * 7
# print(data)
# print((data[3:6]))

# try:
#     raise Exception
# except BaseException:
#     print('1', end='')
# else:
#     print('2', end='')
# finally:
#     print('3', end='')

# nums = [3, 7, 23, 42]
# alphas = ['p', 'p', 'm', 'j']
 
# print(nums is alphas)
# print(nums == alphas)
 
# nums = alphas
 
# print(nums is alphas)
# print(nums == alphas)
# alphas.append("rasna")
# print(alphas)
# print(nums)
# alphas[1]="kalsi"
# print(alphas)
# print(nums)

# def inc(inc):
 
#     def do(val):
#         return val + inc
 
#     return do
 
 
# action = inc(-1)
# print(action(2))

# data = {'one': 'two', 'two': 'three', 'three': 'one'}
# res = data['three']
 
# for _ in range(len(data)):
#     res = data[res]
#     print(_)
 
# print(res)

# data = {'Peter': 30, 'Paul': 31}
# print((data.keys()))
# print(data.items())

# def f(l):
#     return l(-3, 3)
 
 
# print(f(lambda x,y: x if x > y else y))


# print(3 * 'abc' + 'xyz')

# name = 'Peter'
# age = 23
# flag = TRue
# print(type(name),type(age),type(flag))

# from datetime import timedelta
 
# delta = timedelta(weeks=1, days=7, hours=11)
# print(delta * 2)

# productIdList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# index = 0
 
# while index < 10:
#     print(productIdList[index])
#     if productIdList[index] == 6:
#         break
#     else:
#         index += 1


# class Ex(Exception):
#     def __init__(self, msg):
#         Exception.__init__(self,msg+msg)
#         raise Exception("Hello")
#         self.args = (msg,"Rasna")
 
 
# try:
#     raise Ex('ex')
# except Ex as e:
#     print(e)
# except Exception as r:
#     print("inside exception")
#     print(r.args)

# from sys import argv
# print(argv[1] + argv[2])


# class A:
#     def __init__(self,value=True):
#         print("True")

# b=A()
# print()

# strng = '\''.join(("Mary", "had", "21", "sheep"))
# print(strng)
# print(strng[0:1].islower())

# consts = (3.141592, 2.718282)
# try:
#     print(consts[2])
# except Exception as exception:
#     #print(hasattr(exception,args))
#     print(exception.args)
# else:
#     print("('success')")

# class A:
#     x=10
#     def __init__(self,value=10):
#         self.value=value

# a=A()
# print(hasattr(A,"value"))
# x = input('Enter the first number: ')
# y = input('Enter the second number: ')
# print("The result is "+str(int(x)+int(y)))

# import random
# nums=[random.randint(1,7) for i in range(1,8)]
# print(nums)

# class A:
#     def __init__(self):
#         print("inside init fn of A")
#         self.x = 1
 
#     def func(self):
#         self.x = 10
 
 
# class B(A):
#     def __init__(self):
#         print("inside init fn of class B")
#         self.x=10
#     def func(self):
#         self.x += 1
#         return self.x
 
 
# b = B()
# print(b.func())
import copy

# data = {'name': 'Peter', 'age': 30}
# person = data.copy()
# person=copy.copy(data)
# data["name"]="Rasna"
# print(data)
# print(person)
# print(id(data) == id(person))

# l1=[10,20,30]
# l2=copy.copy(l1)

# l2=l1
# print(id(l1)==id(l2))
# l1[1]=200
# print(l1)
# print(l2)
# l1.append(1000)
# print(l1)
# print(l2)

# l1=["Rasna",[4,5,6],[7,8,9]]
# l2=copy.copy(l1)
# print(l1)
# print(l2)
# print(id(l1))
# print(id(l2))
# l2[0]=40
# print(l1)
# print(l2)
# print(id(l2[0]))
# print(id(l1[0]))

# data = (1, 2, 4, 8)
# data = data[-2:-1]
# print(data)
# data = data[-1]
# print(data)

# def func(n):
#     s = ''
#     for i in range(n):
#         s += '*'
#         yield s
 
 
# for x in func(3):
#     print(x, end='')


# 1
# try:
#     value = input("Enter a value: ")
#     assert value==1
#     print(value/value)
# except ValueError:
#     print("Bad input...")
# except ZeroDivisionError:
#     print("Very bad input...")
# except TypeError:
#     print("Very very bad input...")
# except:
#     print("Booo!")
# class X:
#     pass

# class A(X):
#     pass

# class B(X):
#     pass
# class C(B,A):
#     pass

# c=C()
# print(C.__bases__)

# class Alpha:
#     def say(self):
#         return "alpha"
 
 
# class Beta(Alpha):
#     def say(self):
#         return "beta"
 
 
# class Gamma(Alpha):
#     def say(self):
#         return "gamma"
 
 
# class Delta(Beta, Gamma):
#     pass
 
 
# d = Delta()
# b = Beta()
# print(isinstance(d,Alpha))
# print(Gamma in Delta.__bases__)
# print(b is d)
# print(d.say()=="gamma")

# try:
#     print("5" / 0)
# except ArithmeticError:
#     print("arith")
# except ZeroDivisionError:
#     print("zero")
# except TypeError:
#     print("type error")
# except:
#     print("some")

# class Diamond:
#     pass
 
# class Adamant(Diamond):
#     pass
 
 
# class Gem(Diamond):
#     pass


# class Jewel(Gem,Adamant):
#     pass

# j=Jewel()

# def func(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return
 
 
# print(func(func(2)) + 1)

# str1 = 'Peter'
# str2 = str1[:]
# print(str1,str2)
# print(id(str1),id(str2))



# str2[1]="k"
# print(str1,str2)


# data = [1, 2, 3, None, (), [], ]
# print(len(data))

# x = int(input())
# y = int(input())
# print(x + y)

# x = 2

# y = 6

# x += 2 ** 3

# x //= y // 2 // 3

# print(x)

# data = [1, 2, [3, 4], [5, 6], 7, [8, 9],12,"rasna",(10,2)]
# count = 0
 
# for i in range(len(data)):
#     if type(data[i]) == tuple:
#         count += 1
 
# print(count)

# dictionary = {}
# my_list = ['e', 'b', 'c', 'd']
 
# for i in range(len(my_list) - 1):
#     dictionary[my_list[i]] = (my_list[i], )


# print(dictionary)
 
# for i in sorted(dictionary.keys()):
#     #print(i)
#     k = dictionary[i]
#     # Insert your code here.
#     print(k[0])

# print(type(dir()))

# x = 42
 
# def func():
#     global x
#     print('1. x:', x)
#     x = 23
#     print('2. x:', x)
 
 
# func()
# print('3. x:', x)

# def func():
#     text = 'Paul'
#     names = lambda x: text + ' ' + x
#     return names
 
 
# people = func()
 
# print(people('Peter'))

# import random
# print(random.seed(3))

# def func(x1, y):
#     if x == y:
#         return x
#     else:
#         return
 
 
# func(x1, y=1)
# print(func(0, 3))

# class A:
 
#     x = 0
 
#     def __init__(self, v=0):
#         self.y = v
#         A.x += v
 
 
# a = A()
# b = A(1)
# c = A(2)
 
# print(c.x)

# def func(data):
#     data = [7, 23, 42]
#     print('Function scope: ', data)
 
 
# data = ['Peter', 'Paul', 'Mary']
# func(data)
# print('Outer scope: ', data)

# def func(x=2, y=3):
#     return x * y
 
 
# print(func(y=2))

# class Accident(Exception):
#     def __init__(self, message):
#         self.message = message
 
#     def __str__(self):
#         return "problem"
 
 
# try:
#     print("action")
#     raise Accident("accident")
# except Accident as accident:
#     print(accident)
#     print(accident.message)
#     print(accident.args)
# else:
#     print("success")

# s="rhyme"
# s[0]=s[1]
# print(s)

# 
# for line in open('peoples.txt', 'r'):
#     print(line)

# file=open('peoples.txt', 'r')
# print(type(file))
# print(file.readlines())
# file.close()

# my_list = [x * x for x in range(5)]
 
 
# def fun(lst):
#     del lst[lst[2]]
#     return lst
 
 
# print(fun(my_list))


# from sys import argv
# sum = 0
# for i in range(2, len(argv)):
#     sum += float(argv[i])
# print(
#     "The average score for {0} is {1:.2f}"
#     .format(argv[1], sum/(len(argv)-2))
# )


# def func():
#     try:
#         return 1
#     finally:
#         return 2
 
 
# res = func()
# print(res)

# import random
 
# random.seed(0)
# x = random.choice([1, 2])
# random.seed(0)
# y = random.choice([1, 2])
# print(x - y)

# x = 'Peter'
# y = 'Peter'
# print(x,y)

# print(x,y)
# res = x is y
# print(res)

# class Package:
#     spam = ''
 
#     def __init__(self, content):
#         Package.spam += content + ";"
 
 
# envelope_1 = Package("Capacitors")
# envelope_2 = Package("Transistors")
# print(envelope_2.spam)


# marks = [80, 70, 90, 90, 80, 100]

# average = sum(marks) // len(marks)

# grade = ''

# if 90 <= average <= 100:
#     grade = 'A'
# elif 80 <= average < 90:
#     grade = 'B'
# elif 70 <= average < 80:
#     grade = 'C'
# elif 65 <= average < 70:
#     grade = 'D'
# else:
#     grade = 'F'
 
# print(grade)




# x, y, z = 3, 2, 1
# z, y, x = x, y, z
# print(x, y, z)

# class Alpha:
#     value = "Alpha"

#     def say(self):
#         return self.value.lower()


# class Beta(Alpha):
#     value = "Beta"


# class Gamma(Alpha):
#     def say(self):
#         print("inside gamma")
#         return self.value.upper()


# class Delta(Gamma,Beta):
#     pass


# d = Delta()
# b = Beta()
# a=Alpha()
# print(d.say())
# print(b.say())
# print(Delta.mro())

# import math
# s=math.sqrt(16)
# print(s)

# try:
#     raise Exception
# except BaseException:
#     print("a")          # a
# except Exception:
#     print("b")
# except:
#     print("c")

# with open('file', 'w') as f:
#     for i in range(1, 6):
#         f.write(str(i) + '. Line\n')

# for x in open('file', 'rt'):
#     print(x)

# file=open('file',"r")
# l1=file.readline()
# print(l1)

# class Content:
#     _title = "Rasna"

 
#     def __init__(self, name):
#         print("inside init fn")
#         self._name = name

#     def print_name(self):
#         print("inside content print_name fn")
#         print(self.__name)
#         print(Content.__title)
    
# class Content1(Content):
#     def print_name(self):
#         print("inside content1 print_name fn")
#         print(self._name)
#         print(self._title)
 
# c1 = Content1("Paper")
# c1.print_name()
# #print(c1._Content_title)

# def greet(*names):
#     print(type(names))
#     print(names)
#     for name in names:
#         print("Hello ", name)

# greet("Rasna","Rinku","Ruhi","Jia")

# zip1=zip(["Rasna","Rinku","Ruhi","Jia","Ruby"],[1,2,3,4])
# # print(type(zip1))
# # print(list(zip1))
# zipl=list(zip1)
# print(zipl)
# for item in zipl:
#     print(item)
# print("reached outside the for loop")

# x=1
# while x<10:
#     x=x<<1
#     print("*")

# print("" not in "")
# print(" " in "alphabet")


# try:
#     x,y=3,1
#     z=x/y
#     file=open("file.txt","r")
#     for data in file:
#         print(y)
#         print(data,sep=" ")
#         y+=1
        

# except ArithmeticError:
#     z=-1
# else:
#     z=-2
# finally:
#     z=-3
#     x=x-1
#     file.close()
# print(z)
# print(x)
# l1=file.readlines()
# print(l1)
# import sys
# print("Hi Rasna")
# sys.exit()
# print("Bye")
# print("Peter""Wellert")
# l1=[20,30,10,21,29,10]
# print(l1)
# print(l1.sort(reverse=True))
# print(l1)
# import random
# random.shuffle(l1)
# print(l1)
#print(7+None)
# x=7
# y=None
# print(7 is None)
# print(y is None6yjm)
# import sys
# print(sys.path)

# data=(1,2,4,8)
# data=data[-2:-1]
# # print(data)
# # print(type(data))
# # data=data[-2]
# # print(data)

# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
# class D:
#     pass

# print(issubclass(C,(D,B)))
# print(C.__bases__)
# str1="Rasna"
# str2=str1[:887]
# print(str1)
# print(str2)
# print(str1 is str2)
# print(str1 == str2)

# string="\'".join(("Mary", "had", "21","sheep"))
# print(string)
# print(string[0:1].islower())

# def func(data):
#     print(id(data))
#     data=[7, 23, 42]
#     print(id(data))
#     print('Function scope: ', data)  # [7, 23, 42]


# data = ['Peter', 'Paul', 'Mary']
# print(id(data))
# func(data)
# print('Outer scope: ', data)  # ['Peter', 'Paul', 'Mary']
# s="rhyme"
# print(s[::2])
# print()
# print(3+None)
import calendar
#print(calendar.month(2022,5,4,1))
#print(calendar.weekday(2022,5,7))
# print(calendar.monthrange(2022,5))
# print(calendar.monthcalendar(2022,5))
# import copy

# list1=[[1,2,3],[4,5,6]]
# listc=copy.copy(list1)
# listd=copy.deepcopy(list1)
# list2=list1
# print(list1)
# print(listc)
# print(listd)
# print(list2)
# print(id(list1[0]),id(listc[0]),id(listd[0]),id(list2[0]))
# list1[0][1]=10
# print(list1)
# print(listc)
# print(listd)
# print(list2)
# print(id(list1),id(listc),id(listd),id(list2))
# list1.append([100,200,300])
# print(list1)
# print(listc)
# print(listd)
# print(list2)
# import platform
# print(platform.platform())
# print(platform.uname())
# print(platform.python_build())
# print(platform.system())
# print(platform.python_implementation())
# print(platform.python_version())
# print(platform.node())


# data = {1: 0, 2: 1, 3: 2, 0: 1}
# x = 0
 
# for _ in range(len(data)):
#     print(_)
#     x = data[x]
 
# print(x)

# data1 = (1, 2)
# data2 = (3, 4)
# print(data1+data2)
# [print(sum(x)) for x in [data1 + data2]]

# # list1=[x for x in [data1+data2]]
# # print(list1)

# for x in [data1+data2]:
#     print(x)
#     print("hi")


#print(dir(math))
# import math
# x=math.fmod(4,3)
# print(x)
# print(math.frexp(16))
#print(pip.show())

class A:
    cx=None
    def __init__(self):
        self.x=100
    def greet(self):
        print("Hello")
    
    def remove(self):
        del self.x

a=A()
print(a.__dict__)
print(A.__dict__)
print('x' in a.__dict__)
a.remove()
print("x" in a.__dict__)
print(A.__dict__["cx"]!=None)