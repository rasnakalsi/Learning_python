import os
from os import path
import datetime
from datetime import date,time,timedelta
import time

#Print name of os
print(os.name)

#Check for item existence and type
print("Item exists: ",str(path.exists("textfile.txt")))
print("Item is file: ",path.isfile("textfile.txt"))
print("Item is dir:",path.isdir("textfile.txt"))

##Working with filepaths
print("\nWorking with file paths\n")
fp=path.realpath("textfile.txt")
print(fp)
print("\nItems path and name : ",path.split(fp))

##Getting modification time of the file
mtime=path.getmtime("textfile.txt")
ct=time.ctime(mtime)
dt=datetime.datetime.fromtimestamp(mtime)
print("File modification time",mtime)
print("File mtime in ctime format: ",ct)
print("File mtime in dtime format: ",dt)

##Calculating how long ago the file was .modified
td=datetime.datetime.now()-datetime.datetime.fromtimestamp(mtime)
print("It has been ",td," since the file was modified")
print("or",td.total_seconds()," seconds")
