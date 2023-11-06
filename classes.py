class Animal:
    def walk(self):
        print("walking...")


class Dog(Animal):
    # initiates one or more properties when the class is created
    def __init__(self, name, age):
        """INITIATES A NEW DOG"""
        self.name = name
        self.age = age

    def bark(self):
        print("woof!")


roger = Dog("Roger", 5)
print(roger.name)

roger.bark()
roger.walk()
print(help(roger))
