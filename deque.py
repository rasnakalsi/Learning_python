import collections
import string

def main():
    d=collections.deque(string.ascii_lowercase)

    print(d)

    #using len fn to determine length of deque
    print("No of items in deque ",str(len(d)))

    #deque can be iterated over
    for elem in d:
        print(elem.upper(),end=",")
    print("\n")

    #manipulate item on either end
    print("Original deque \n ",d)
    d.pop()
    d.popleft()
    d.append(26)
    d.appendleft(1)
    print(d)
    
    ##performing rotate operation
    dc=d.copy()
    print(d)
    d.rotate(5)
    print("d= ",d)
    print("dc ",dc)
    dc.rotate(-5)
    print(dc)


if __name__=="__main__":
    main()
