import os

# file handling
# reading a file
readFile = open("demofile.txt", "r")
# print(readFile.read())

# read line after line
print(readFile.readline())

# specify file path if not found in the current directory
# f = open("home\daniel:\\py-space\Day-1\py_intro.py", "r")
# print(f.read())

# writing to an existing file
# f2 = open("demofile2.txt", "a")
# f2.write("This is a new file just recently created!!")
# f2.close()
# f2 = open("demofile2.txt", "r")
# print(f2.read())

f2 = open("demofile2.txt", "w")
f2.write("woops I've deleted the file!")
f2.close()
f2 = open("demofile2.txt", "r")
# print(f2.read())

# remove a file
os.remove("demofile2.txt")
print("file removed")