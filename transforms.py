def filterFunc(x):
    if x%2 ==0:
        return False
    return True

def filterFunc2(x):
    if x.islower():
        return True
    return False

def squareFunc(x):
    return x**2

def toGrade(x):
    if x>90:
        return "A"
    elif x<=90 and x>80:
        return "B"
    else:
        return "C"

def main():
    nums=[1,2,3,5,44,32,11,91]
    chars="ancRtWcSHop"
    grades=(80,99,100,32,98)

    odds=list(filter(filterFunc,nums))
    print(nums)
    print(odds)

    lowers=list(filter(filterFunc2,chars))
    print(chars)
    print(lowers)
    
    num=[1,3,4,7,8,9,0]
    squares=list(map(squareFunc,num))
    print(num)
    print(squares)

    grades=sorted(grades)
    letters=list(map(toGrade,grades))
    print(grades)
    print(letters)

print(entities())

from datetime import date
 
date_1 = date(1992, 1, 16)
date_2 = date(1991, 2, 5)
 
print(date_1 - date_2)


if __name__=="__main__":
    main()

