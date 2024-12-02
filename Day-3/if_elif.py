from random import randint

a = 33
b = 200

if b > a:
    print("b is bigger than a")
elif b == a:
    print("b and a are equall")
else:
    print("a is lesser than b")

# if else short hand
a = 2
b = 330
# print("A") if a > b else print("B")

# guessing game
magic_num = randint(1, 10)

# User enters a value
val = int(input("Enter a value between 1 and 10 : "))
# for (guessCount = 3)
if val > magic_num:
    print("Value too high")
    # int(input("Enter a value again: "))
elif val == magic_num:
    print("Guess successful!")
else :
    print("Guess too low")
    # int(input("Enter a value again: "))