#
f=0
print(f)
#redeclaring the variables work
f="abc"
print(f)

##Variables of different types cannot be combined
print("This is a string "+str(123))

##Local versus global variable
f=0
def someFunction():
    global f ##comment/uncomment this line to see the variation in output
    f="def"
    print(f)
someFunction()
print(f)
del f ## deletes the definition of variable f
print(f) ##raises error as variable is now undefined

