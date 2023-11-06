class Dog:
    def eat(self):
        print("Eating dog food!")


class Cat:
    def eat(self):
        print("Eating cat food!")


animal1 = Dog()
animal2 = Cat()
animal1.eat()
animal2.eat()


# operator overload
class Camel:
    # initiates one or more properties when the class is created
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return True if self.age > other.age else False


roger = Camel('Roger', 8)
syd = Camel('Syd', 60)

print(roger > syd)