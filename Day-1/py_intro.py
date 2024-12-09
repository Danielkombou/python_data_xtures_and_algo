# import sys


# # introducing python to Dan's codefolio
# print("Hello momma")
# # print(sys.version)

# x = str(5)
# # print(type(x))
# u = 3.2
# a = int(u)
# # print(a)
# # key concepts to be noted
# # Abstraction, Encapsulation, polymorphism, inheritance = "noted"
# num1 = "52"
# # print(num1.isnumeric())

# txt = "The first of our class is a male person"
# # print("free" not in txt)
# # print(txt[2:6])

# x = 'Wel, come'
# # print(x.replace('W', 'B'))
# print(x.split(","))



# list
# tuple 
# dictionary
# set

# ## list
# favorites = [8, "Banana", 'c', 2]

# # favorites.pop()
# # favorites.remove("Banana")

# list_copy = favorites[:]

# list_copy[0] = True

# print(list_copy)
# print(favorites)

import operator
itg = operator.itemgetter 
atg = operator.attrgetter

# # tuple
# favorites = (8, "banana", 2)

# index = favorites[:]
# print (index)


# print(favorites)

# dictionary

# cars = {"model": "toyota", "Year": 2023, "brand": "carina"}

# print(cars["model"])

# favorites = [{'model': 3, "mark": 2}, {"model2": 3, "mark2": 3}]

# print(favorites[0]["model"])

# for key in favorites[0].items():
#     print(key)


# set
# colors1 = {"blue", "green", "yellow", "red"}
# colors1.add("purple")

# print (colors1)

# for item in colors1:
#     print(item)

# print(colors1)

# colors2 = {["hello", "there"], "orange", "purple", "magenta"}


# print(colors2)

text = "good hello everyone in here!"
print(text.find("h"))