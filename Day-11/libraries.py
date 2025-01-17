from random import randint, choice
import math

x = randint(1, 9)

# using choice fxn which takes list and tuple
players = ['Charles', 'Matina', 'Michael', 'Florence', 'Eli']
first_up = choice(players)
print(first_up)