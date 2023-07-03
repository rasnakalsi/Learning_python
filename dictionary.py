def main():
    ctemps=[0,12,34,100]

    #using comprehension to build a dictionary
    tempDict={t:(t*9/5)+32 for t in ctemps}
    print(tempDict)
    print(tempDict[12])

    sub1={"English":32,"Hindi":67,"French":99}
    sub2={"Maths":89,"Science":98}
    totals=[t for t in (sub1,sub2,ctemps)]
    #print( for t in (sub1,sub2))
    print(totals)
    totals={ k:v for sub in (sub1,sub2) for k,v in sub.items()}
    print(totals)

if __name__=="__main__":
    main()
