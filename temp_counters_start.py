from collections import Counter

def main():

    class1=["Apple","Orange","Kiwi","Water melon"]
    class2=["Apple","Orange","Kiwi","Kiwi","Mango","Pears","Pears","Pears","Pears","Pears","Pears"]

    c1=Counter(class1)
    c2=Counter(class2)

    print(class1)
    print(class2)

    print("Original class2 , before doing subtraction")
    print(sum(c2.values())," fruits exist in class2")
    print(c2.most_common())

    #subtracting class1 from class2
    print("After subtracting class1 from class2")
    c2.subtract(c1)
    print(sum(c2.values()),"fruits exist in class2")
    #ERROR : output of above line shows wrong count7 instead of 8
    ## Reason for above wrong output is inclusion of "Water melon " ,
    ##  as shown in output of class2.most_common() function with value of -1
    print(c2.most_common())


if __name__=="__main__":
    main()

