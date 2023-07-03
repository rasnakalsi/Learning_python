from dataclasses import dataclass
#Case1 : dataclass not frozen
# @dataclass
# class ImmutableClass:
#     value1:str="Value1"
#     value2:int=0

# obj=ImmutableClass()
# print(obj.value1)

##Case2: dataclass is frozen and modifying object from outside
@dataclass(frozen=True)
class ImmutableClass:
    value1:str="Value1"
    value2:int=0
    ##Case 3: modifying value from within class defn
    def somefunc(self,newval):
        self.value2=newval


obj=ImmutableClass()
print(obj.value1)

##Case2: modifying variable value from outside class
# obj.value1="Rasna"
# print(obj)

##Case3: Modifying variable from within the class
obj.somefunc(20)
print(obj)