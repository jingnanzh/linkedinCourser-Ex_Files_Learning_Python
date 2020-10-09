#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
import time
from shutil import make_archive #for zip archive
from zipfile import ZipFile

def main():
  # make a duplicate of an existing file
  if path.exists("textfile.txt"):

    # get the path to the file in the current directory
    src = path.realpath("textfile.txt")
    
    # let's make a backup copy by appending "bak" to the name
    dst =  src + ".bak"

    # copy over the permissions, modification times, and other info
    # shutil.copy(src,dst)
    # t = time.ctime(path.getmtime("textfile.txt.bak"))
    # print(t) #Thu Oct  8 12:01:23 2020
    #
    # shutil.copystat(src,dst)
    # t = time.ctime(path.getmtime("textfile.txt.bak"))
    # print(t) #Wed Oct  7 20:39:47 2020

    # rename the original file
    # os.rename("textfile.txt", "textfile.txt")
    
    # now put things into a ZIP archive
    # root_dir,tail = path.split(src) #only need the path, not with file name
    # print(root_dir)
    # shutil.make_archive("archive", "zip", root_dir)

    # more fine-grained control over ZIP files
    with ZipFile("testzip.zip", "w") as newzip:
      newzip.write("textfile.txt")
      newzip.write("textfile.txt.bak")
      
if __name__ == "__main__":
  main()
