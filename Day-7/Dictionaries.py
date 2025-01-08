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
# for x in thisdict:
#   print(x, thisdict[x])

# for u, i in thisdict.items():
#   print(u, i)

# Nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# print(myfamily["child1"]["name"])

for dict1, obj in myfamily.items():
    print(dict1)
    for it in obj:
        print(it + ":", obj[it])