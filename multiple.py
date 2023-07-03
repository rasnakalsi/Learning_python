class A:
    def __init__(self):
        super().__init__()
        self.foo="foo"
        self.name="Class A"
        print("Inside init of class A,initialising foo")

class B:
    def __init__(self):
        super().__init__()
        self.bar="bar"
        self.name="Class B"
        print("Inside class B, initialising bar")

class C(B,A):
    def __init__(self):
        super().__init__()
    
    def showprops(self):
        print(self.foo)
        print(self.bar)
        print(self.name)

c=C()
c.showprops()
print(C.__mro__)