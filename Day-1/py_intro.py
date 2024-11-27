import sys
from datetime import datetime


# introducing python to Dan's codefolio
print("Hello momma")
# print(sys.version)

x = str(5)
# print(type(x))
u = 3

# Many to many values assignment to variables
a, b, c = "Orange", "Apple", "Pear"
# print(a)
# print(b)
# print(c)

# one value to many variables
q = w = e = "cherry"
# print(q)

# Unpacking a collection
fruits = ["boy", 4, "banana"]
f, r, u = fruits
# print(f, r, u)

# output variable using +
p = "Python "
y = "is "
t = "awesome"
print(p + y + t)


"global variables"
even = 2
def firstFxn() :
    print(even, "is an even number")
firstFxn()

def displayNumber() :
    global even
    even = 4
    print(even, "is an even number")
# displayNumber()
# print(even)

# program to display user's age
currentDate = datetime.now()

name = input("Enter your name: ")
day = int(input("Enter you day of birth: "))
month = int(input("Enter your month of birth: "))
year = int(input("Enter your year of birth: "))



birthDay = datetime(year, month, day)
# ageInYears = currentDate.year - birthDay.year
# ageInDays = (currentDate.year - birthDay.year).days
# print(ageInDays)
userAge = int(currentDate.year - year)
userAgeInDays = userAge * 365
print(f"Dear {name} you are {userAge} years old")
print(f"Dear {name} you are approximately {userAgeInDays} days old")