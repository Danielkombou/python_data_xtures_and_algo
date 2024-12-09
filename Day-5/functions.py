import math

# Li = ["ball", 32, 3.222, False, "banana"]

# # for l in Li:
# # print(l)

# for idx in range(len(Li)):
#     print(idx)

x = math.ceil(5.2)
# print(x)


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
result = basic_operations(9, 4, 'add')
print(result)