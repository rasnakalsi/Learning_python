from collections import OrderedDict
def main():
    sportTeams=[("Black",(10,2)),("Yellow",(3,10)),("Pink",(20,3)),("Orange",(5,2)),("Blue",(22,9))]

    sortedTeams=sorted(sportTeams,key=lambda t:t[1][0],reverse=True)

    print("Original sportTeams: ",sportTeams)

    print("Sorted Teams",sortedTeams)

    ## Create an ordered dictionary of items
    teams=OrderedDict(sortedTeams)
    print(teams)

    for i,team in enumerate(teams,start=1):
        print(i,team)
        if i==4:
            break
    
    for key in teams.keys():
        print(key)
    
    for key,item in zip(teams.keys(),teams.values()):
        print(key,item)


    ##popitem
    print("Original teams \n",teams)
    key,value=teams.popitem(False)
    print("Top item is :",key,value)

    print("After removing top item\n",teams)
    key,value=teams.popitem()
    print("Last item of dictionary is :",key,value)
    print("After removing last item \n",teams)

    ##equality1=comparing two ordered dictionaries
    d1=OrderedDict({"a":1,"b":2,"c":3})
    d2=OrderedDict({"a":1,"b":2,"c":3})
    d3=OrderedDict({"a":1,"c":3,"b":2})
    print("d1=",d1)
    print("d2=",d2)
    print("d3=",d3)

    print("Result of Equality test d1==d2 :",d1==d2)
    print("Result of Equality test d1==d3 :",d1==d3)



    ##equality 2
    od=OrderedDict({"a":1,"b":2,"c":3})
    d={"a":1,"c":3,"b":2}
    print("od=",od)
    print("d=",d)
    print("Equality test od==d",od==d)


if __name__=="__main__":
    main()