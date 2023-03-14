

class Person:
    def __init__(self, age, name1, name2):
        self.age = age
        self.name1 = name1
        self.name2 = name2

        print("Age: " + str(age) + ", Name: " + name1 + " " + name2)


user = Person(14, "Judah", "Starkenburg")