##Demonstrate the use of docstrings

def myFunction(arg1,arg2=None):
    """ myFunction(arg1,arg2=None)

    Parameters:
    arg1: the first argument, whatever you feel like entering
    arg2: the second argument, defaults to None

    """
    print(arg1,arg2)


def main():
    print(myFunction.__doc__)


if __name__=="__main__":
    main()

