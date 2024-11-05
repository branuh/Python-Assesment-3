class Engine:
    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()

    def stop_car(self):
        self.engine.stop()

# Create a car object
car = Car()

# Start and stop the car's engine
car.start_car()
car.stop_car()