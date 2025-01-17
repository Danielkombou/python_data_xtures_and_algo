# working with classes
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        '''Initializing name and age attribute'''
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is sitting")

    def rolling(self):
        print(f"{self.name} is rolling")

my_dog = Dog("Mamus", 6)
# print(f"my dog's name is {my_dog.name}")
# print(f"my dog is {my_dog.age} years old")

# my_dog.sit()

# restaurant exercise
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name}!")
        print(f"The cuisine here is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"This resto is always open")


my_resto = Restaurant("Santos", "Spices")
# print(f"{my_resto.restaurant_name} is my favorite restaurant!")
# print(f"The cuisine type here's {my_resto.cuisine_type}")

# my_resto.describe_restaurant()