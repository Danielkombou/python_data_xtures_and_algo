import os

# file handling
# reading a file
readFile = open("demofile.txt", "r")
# print(readFile.read())

# read line after line
# print(readFile.readline())

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
# print("file removed")
print(os.listdir())

def read_save():
    # create a new file in this directory
    execisefile = input("Enter the file name: ")
    file_name = open(execisefile, "x")
    file_name.close()

    text_content = input("Add content to the file: ")
    file_name = open(execisefile, "w")
    file_name.write(text_content)
    file_name.close()
    file_name = open(execisefile, "r")
    print(file_name.read())

# read_save()