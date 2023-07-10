class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

car = Car("Toyota", "Camry", 2022, 4)
print("Make:", car.make)
print("Model:", car.model)
print("Year:", car.year)
print("Number of doors:", car.num_doors)