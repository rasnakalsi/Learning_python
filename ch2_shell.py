import os
from os import path
import shutil
from shutil import make_archive

if path.exists("textfile.txt"):
    #get the path to the file in current dir
    src=path.realpath("textfile.txt")

    #lets make a backup using of .txt by appending .bak at the end
    dst=src+".bak"
    shutil.copy(src,dst)

    #Renaming textfile.txt as newfile.txt
    os.rename("textfile.txt","newfile.txt")

    #Making archive of files print in current dir where textfile.txt exists
    root_dir,tail=path.split(src)
    shutil.make_archive("rasna","zip",root_dir)