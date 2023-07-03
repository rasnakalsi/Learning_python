import itertools

def main():
    seq1=["Joe","John","Mike"]
    cycle1=itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))


    count1=itertools.count()
    print(next(count1))
    print(next(count1))
    print(next(count1))

    vals=(10,20,30,40,50)
    print(vals)
    acc=itertools.accumulate(vals)
    print(list(acc))

    vals=(10,20,30,40,50,90,100,32)
    print(vals)
    acc=itertools.accumulate(vals,max)
    print(list(acc))
    
    x=itertools.chain("ABCD","1245")
    print(list(x))

    def testFunc(x):
        if x<40:
            return True
        else:
            return False

    print(vals)
    print(list(itertools.dropwhile(testFunc,vals)))
    print(list(itertools.takewhile(testFunc,vals)))


if __name__=="__main__":
    main()

    
