myfile=open("textfile.txt","w+")
for i in range(5):
    myfile.write("This is some text \n")

myfile.close()

## Adding content to existing file using append(a+) mode
myfile=open("textfile.txt","a+")
for i in range(6):
    myfile.write("This is new text\n")

myfile.close()

## Reading the file. If you open a file for reading, there is no need to close the file
## Case1: Reading entire content of file via read() fn

myfile=open("textfile.txt","r")
if myfile.mode=="r":
    contents=myfile.read()
    #print(contents) ##uncomment this line if you want to see the contents read via read() fn

#using readlines() to read the file one line at a time and store the lines read in a list , here in f1
myfile=open("textfile.txt","r")
if myfile.mode=="r":
    f1=myfile.readlines()
    for x in f1:
        print(x)
        print("*"*99)
print(f1)



