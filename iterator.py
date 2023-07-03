def main():

    days=["Sun","Mon","Tues","Wed","Thu","Fri","Sat"]
    daysFr=["Dim","Lun","Mar","Mer","Jeu","Ven","Sam"]

    #create an iter over days collection
    # i=iter(days)
    # print(i)
    # print(next(i))
    # print(next(i))
    # print(next(i))

    # with open("textfile.txt","r") as fp:
    #     for line in iter(fp.readline,""):
    #         print(line)

    #looping over  collections
    # for m in days:
    #     print(m)

    # #Generating index along with data

    # for m in range(len(days)):
    #     print(m+1,days[m])


    # for i in enumerate(days,start=10):
    #     print(i)
    
    # for i,d in enumerate(days,start=20):
    #     print(i,d)


    # for m in zip(days,daysFr):
    #     print(m)    
    
    # days=["Sun","Mon","Tues","Wed","Thu","Fri","Sat"]
    # daysFr=["Dim","Lun","Mar","Mer","Jeu"]

    # for m in zip(days,daysFr):
    #     print(m)
    
    for i,m in enumerate(zip(days,daysFr)):
        print(i,m[0]," = ",m[1]," in French")


if __name__=="__main__":
    main()