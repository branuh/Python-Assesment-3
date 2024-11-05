class Cat:
    def make_sound(self):
        print("Meow")

class Dog:
    def make_sound(self):
        print("Woof")

def animal_sound(animal):
    animal.make_sound()

# Create instances of Cat and Dog
cat = Cat()
dog = Dog()

# Call the animal_sound function with different objects
animal_sound(cat)  # Output: Meow
animal_sound(dog)  # Output: Woof