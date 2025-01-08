# create a set
myset = {"apple", "banana", "mango"}

# different data types
set1 = {"abc", 34, True, 40, "male"}
# print(set1)

# add items in a set
set1.add("yoga")
# print(set1)

# adding two sets
tropical = set(("papaya", "guava", "mango"))
set1.update(tropical)
# print(set1)

# adding any iterable
mylist = ["kiwi", "orange"]
# set1.update(mylist)
# print(set1)

# remove item from a set
# use remove() to remove a single specied item
# pop() remove randomly
# clear() empties the entire set

# joining sets or (|)
set3 = set1.union(tropical, myset)
# print(set3)
set4 = myset | myset
# print(set4)

# set and tuples can be joined

# intersection and &
# print(myset, set1)
# print(myset.intersection(set1))

setX = {"apple", 1,  "banana", 0, "cherry"}
setY = {False, "google", 1, "apple", 2, True}

setZ = setX.intersection(setY)
# print(setZ)

# difference or - operator
difSet = setX.difference_update(setY)
# print(difSet)
# print(setX)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference(set2)

# print(set1)


# creating a program that finds the intersection between sets

firstSet = {}
secondSet = {}

def interSet():
    firstSet = input("enter the elements of the first set: ").split()
    firstSet = set(firstSet)
    print(f"this is the set with it's elements {firstSet}")
    secondSet = input("Enter the items of set two: ").split()
    secondSet = set(secondSet)
    print(f"this is the set with it's elements {secondSet}")

    choice = input("enter yes to see the intersection between them: ")
    if choice:
        commonValue = firstSet.intersection(secondSet)
        if not commonValue:
            print(f"Oops sorry there is nothing common btn them")
        else: print(f"The common element(s) between them is/are {commonValue}")

interSet()