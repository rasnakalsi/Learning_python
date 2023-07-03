def addition(*args):
    result=0
    for i in args:
        result+=i
    return result

def main():
    print(addition(10,20,30,40))
    print(addition(1,2))
    list1=[10,20,40]
    print(addition(*list1))


if __name__=="__main__":
    main()
