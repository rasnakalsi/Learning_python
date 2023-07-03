import collections
def main():
    Point=collections.namedtuple("point","x y")
    p1=Point("10",30)
    p2=Point(30,40)

    print(p1,p2)

    print(p1.x, p2.y)
    print(type(p1.x))

    p3=p1._replace(x=100)
    print(p3)
    print(p1)

    print(p3==p1)

    # p4=p1.copy()
    # print(p1==p4)


if __name__=="__main__":
    main()

