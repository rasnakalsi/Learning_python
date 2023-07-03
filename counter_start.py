from collections import Counter
def main():
    class1=["Apple","Orange","Orange","Orange","Apple","Banana","Apple","Kiwi","Kiwi","Kiwi","Kiwi"]
    class2=["Apple","Orange","Kiwi","Kiwi","Mango","Pears","Pears","Pears","Pears","Pears","Pears"]

    class1=["Apple","Orange","Kiwi","Water melon"]
    class2=["Apple","Orange","Kiwi","Kiwi","Mango","Pears","Pears","Pears","Pears","Pears","Pears"]


    c1=Counter(class1)
    c2=Counter(class2)


    print(class1)
    print(class2)


    print(c1["Orange"])
    print(c1["Mango"])

    print(sum(c1.values())," fruits exist in class1")

    # c1.update(c2)
    # print(sum(c1.values())," fruits exist in class1")

    # print(c1.most_common(3))


    # print(c1.most_common())
    print(sum(c2.values())," fruits exist in class2")
    print("After subtracting class2 from class1")
    print(c2.most_common())
    c2.subtract(c1)
    print(sum(c2.values())," fruits exist in class2")
    print(c2.most_common())

    # print("After subtracting class2 from class1")
    # print(c1.most_common())
    # c1.subtract(c1)
    # print(sum(c2.values())," fruits exist in class2")
    # print(c1.most_common(3))

    # print("Common items b/w class1 and class2")
    # print(c1 & c2)


if __name__=="__main__":
    main()