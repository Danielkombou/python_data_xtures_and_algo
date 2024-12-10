# lakes = ["superior", "erie", "huron", "ontario", "powell"]
# # print(len(lakes))
# # print(any(lakes))
# lakes.append("nyon")
# # print(lakes)


# list_items = input("Enter list items separated with spaces").split()
# print(f"List of items are {list_items}")
# add_new = input("Add a new item in the list: ")
# new_item = list_items.append(add_new)
# print(f"List of items are {list_items}")
# remove_item = input("Enter the item you wanna remove: ")
# new_item = list_items.remove(remove_item)
# print(f"List of items are {list_items}")


# # contact@ticsummit.org

thislist = ["apple", "banana", "cherry"]
# Add items in a list
thislist[1:2] = ["blackcurrant", "watermelon"]
# print(len(thislist))
thislist.insert(3, "yam")
# print(thislist)

thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
# print(thislist)

# delete an item from a list
thislist1 = ["apple", "banana", "cherry"]
del thislist1[0]
print(thislist1)
# Empty the entire list
thislist1.clear()
print(thislist1)

# Loop over a list
# for x in thislist:
#     print(x)

# looping through list using the len and range method
# for i in range(len(thislist)):
#     print(thislist[i])

# list comprehension
# syntax
# newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits if x != "apple"]
print(newlist)

num = [n for n in range(1, 11) if n < 5]
print(num)
