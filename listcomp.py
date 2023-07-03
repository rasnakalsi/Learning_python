def main():
    evens=[2,4,6,8,10,12,14,16,18,20]
    odds=[1,3,5,7,9,11,13,15,17,19]
    print("Using lambda function to compute squares of values")
    evenSquared=list(map(lambda x: x**2,evens))
    print(evenSquared)
    
    print("Using list comprehension to get Square of numbers")
    evenSquared=[x**2 for x in evens]
    print(evenSquared)
    
    print("Computing squares of odd numbers less than 10")
    oddSquared=[x**2 for x in odds if x<10]
    print(odds)
    print(oddSquared)




if __name__=="__main__":
    main()
