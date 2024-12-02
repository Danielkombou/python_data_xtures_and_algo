from random import randint

# counter = 0
# while counter <= 10:
#     print(counter)
#     counter += 1

# guessing game
guessCounter = 1
randNumber = randint(1, 10)


# while guessCounter <= 4:
#     userNumber = input("Enter a number between 1 and 10: ")
#     if not userNumber.isnumeric():
#         print("please enter numeric values")
#         continue
#     userNumber = int(userNumber)
#     if userNumber < 1 or userNumber > 10:
#         print("Enter number within 1 and 10 including them")
#         continue
#     if userNumber > randNumber:
#         print("Sorry try again")
#         print(f"You have {4-guessCounter} trials left")
#         guessCounter += 1
#     elif userNumber < randNumber:
#         print("Oops number incorrect, get another trial")
#         print(f"You have {4-guessCounter} trials left")
#         guessCounter += 1
#     elif userNumber == randNumber:
#         print("Congrats that's awesome!!")
#         break
#     else:
#         print("Number of guess reached sorry!")
#         break


#  multiplication table generator
# multiplier = input("Please enter a multiplier: ")
# if not multiplier.isnumeric():
#     print("Please enter a numeric value!")
# multiplier = int(multiplier)

# multiplicationValue = 1
# while multiplicationValue <= 12:
#     if multiplier == 0:
#         print("The multiplication table of 0 is 0")
#     break
# if multiplier:
#     multiTable = multiplier * multiplicationValue
#     print(multiplier)
#     multiplicationValue += 1

timeser = 1
multiplier = input("Enter a number: ")
if not multiplier.isnumeric():
    print("Enter a numeric value: ")
    
else:
    multiplier = int(multiplier)
    while timeser <= 12:
        multiTable = multiplier * timeser
        print(multiTable)
        timeser += 1
