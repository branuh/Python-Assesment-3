class Animal:
    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

# Create a Dog object
my_dog = Dog()

# Use inherited methods
my_dog.eat()
my_dog.sleep()

# Use the specific Dog method
my_dog.bark()