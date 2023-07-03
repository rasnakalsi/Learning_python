def ctof(temp):
    return (temp*9/5)+35

def ftoc(temp):
    return (temp-32)*5/9

def main():
    ctemps=[0,12,34,100]
    ftemps=[32,65,100,212]

    print(list(map(ftoc,ftemps)))
    print(list(map(ctof,ctemps)))

    print(list(map(lambda t:(t*9/5)+35,ctemps)))
    print(list(map(lambda t:(t-32)*5/9,ftemps)))


if __name__=="__main__":
    main()
