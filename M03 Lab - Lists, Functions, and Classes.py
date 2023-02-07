class Vehicle:
    def __init__(self):
        self.type = (input("Enter your vehicle type: "))

class Automobile(Vehicle):
    def __init__(self, type):
        super().__init__(type)
        self.year = input("Enter your car year: ")
        self.make = input("Enter your car make: ")
        self.model = input("Enter your car model: ")
        self.doors = input("Enter the number of doors on your car: ")
        self.roof = input("Enter the type of roof on your car: ")

    def displayCar(self):
        print("Vehicle Type: " + Vehicle.type)
        print("Year: " + self.year)
        print("Make: " + self.make)
        print("Model: " + self.model)
        print("Number of doors" + str(self.doors))
        print("Type of roof: " + self.roof)

carType = Vehicle()
carDetails = Automobile()
Automobile.displayCar()