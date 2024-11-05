class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2023)

# Call the display_info() method
my_car.display_info()