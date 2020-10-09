Question 1 of 5
You need to print the content of the "list.txt" file to the console. Which code can you use, assuming the file must already exist and must not be overwritten or created?

You are correct!
f=open("list.txt",'r')
print(f.read())

Question 2 of 5
While _____ checks whether a path exists, _____ checks whether a path is a file.

You are correct!
path.exists(); path.isfile()

Question 3 of 5
How would you improve the code below?
f = open("myfile.txt", "r")
contents = f.read()

You are correct!
Check that f.mode == 'r' before calling f.read() to read from the file.

Question 4 of 5
Your program already imported the ZipFile module using from zipfile import ZipFile. How can you leverage this module to create a new zip archive and add a file to it?

You are correct!
with ZipFile("archive.zip","w") as newzip:
   newzip.write("file.txt")


Question 5 of 5

What is the difference between shutil.copy() and shutil.copystat() functions?
You are correct!
While shutil.copy() copies the file content, shutil.copystat() copies the file metadata.
