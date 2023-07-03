def main():
    l1=[1,2,3,4,5,6,4,2]
    tl1=[ x**2 for x in l1]
    print(tl1)
    tl2={x**2 for x in l1}
    print(tl2)

    string1="Hello Rasna what are you doing rasna HELLO"
    chars={ ch.lower() for ch in string1 if not ch.isspace()}
    print(chars)

    
if __name__=="__main__":
    main()

