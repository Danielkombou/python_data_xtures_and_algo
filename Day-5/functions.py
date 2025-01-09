import math

# Li = ["ball", 32, 3.222, False, "banana"]

# # for l in Li:
# # print(l)

# for idx in range(len(Li)):
#     print(idx)

x = math.ceil(5.2)
# print(x)


# parameters and arguments, use asterick(*) when number of args are unknown
def my_function(*kids):
    print("The youngest child is " + kids[0])


# my_function("Emil", "Tobias", "Linus")


# passing a list as a parameter
def myListfxn(food):
    for x in food:
        print(x)


fruita = ["pear", "bananas", 1]
# myListfxn(fruita)


# creating a reuseable fxn
def basic_operations(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        if b != 0:
            return a / b
        else:
            print("Error: Division by is undefine")
    else:
        return "Invalid operation"


result = basic_operations(a=9, b=4, operator="add")
# print(result)


# Recursion
def tri_recursion(k):
    if(k > 0):
        answer = k + tri_recursion(k - 1)
        print(answer)
    else:
        answer = 0
    return answer

print("recursion example")
tri_recursion(6)

# lambda function
x = lambda a : a + 10
# print(x(5))
# multiple args
x = lambda a, b : a * b
# print(x(5, 6))
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

# print(mydoubler(11))
