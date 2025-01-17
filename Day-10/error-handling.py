# handling errors using the try-except method

# try:
#     f = open("demofile.txt", "a")
#     try:
#         f.write("It's a cute language to study though!!")
#         f = open("demofile.txt", "r")
#         print(f.read())
#     finally:
#         f.close()
# except IOError:
#     print("Oops an error occured")


# calculator project
def calculator():
    try:
        # Get user input
        while True:
            num1 = input("Enter the first numeric value: ")
            if not num1.isnumeric():
                print("Enter numeric values")
                continue
            num1 = int(num1)
            operator = input("Enter the operator (+, -, *, /): ")
            num2 = input("Enter the second value: ")
            if not num2.isnumeric():
                print("Enter numeric values")
            num2 = int(num2)

            # Do the operations
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Can't divide a number by zero")
                result = num1 / num2
            else:
                raise ValueError("Invalid operator")
            print(f"The result is: {result}")
            break
    except ValueError as ve:
        print(f"Input error: {ve}")
    except ZeroDivisionError as zde:
        print(f"Invalid operation: {zde}")
    except Exception as ex:
        print(f"An unexpected error occcured: {ex}")
    finally:
        print("Operation completed succcessfully")


calculator()


# pygame library