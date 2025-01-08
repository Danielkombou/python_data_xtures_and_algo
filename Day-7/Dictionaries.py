# Dictionaries are used to store data values in key: value pairs
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict["model"]
# can also use the get method eg thisdict.get("model")
# print(x)

# get the list of keys
# print(thisdict.keys())


# get the values in the dict
# print(thisdict.values())

# get items as tuples in list
y = thisdict.items()
# print(y)

# checking if a key exist in a dict
# if "model" in thisdict:
#     print("yes model truely there")

thisdict["brand"] = "Nissan"
thisdict.update({"year": 2022})
thisdict.update({"color": "blue"})
# print(thisdict)

# looping over dictionaries
for x in thisdict:
  print(x)

