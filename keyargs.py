def myFunction(arg1,arg2,*,supressException):
    pass

def main():
    #myFunction(1,2,True)
    myFunction(1,2,supressException=True)



if __name__=="__main__":
    main()

