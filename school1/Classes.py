
first_name = input('First Name: ')
last_name = input('Last Name: ')
age = input('Age: ')
height = input('Height: ')
favorite_food = input('Favorite Food: ')
weight = input('Weight: ')

class Person:
    def __init__(self, age, weight, height, first_name, last_name, favorite_food):
        
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name
        self.favorite_food = favorite_food

user = Person(age, weight, height, first_name, last_name, favorite_food)