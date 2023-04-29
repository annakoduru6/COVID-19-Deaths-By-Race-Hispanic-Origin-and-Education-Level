class Vehicle: 

    def __init__(self, color, year, make, model, mileage = 0):
        self.color = color
        self.year = year
        self.make = make
        self.model = model
        self.mileage = mileage
    

    def honk(self):
        return "HOOOOOOONK!"
    
    def drive(self, miles_driven):
        self.mileage <= miles_driven
        return self.mileage
    
# More specific "Child" class

class Car(Vehicle):
    # Static Attribute 
    # can't be changed via user input to the contructor
    num_wheels = 4
    
    def __init__(self, color, year, make, model, style, mileage=0, top_open = False):
        super().__init__(color, year, make, model, mileage)
        self.style = style
        self.top_open = top_open

    def raise_roof(self):
        if (self.top_open):
            return "top is already open"
        else:
            self.top_open = True
            return "top is now open"

    def lower_roof(self):
        if (self.top_open):
            self.top_open = False
            return "top is now closed"
        else:
            return "top is already closed"

if __name__ == '__main__':
    my_vehicle = Car('red', 2022, "Porsche", "Boxter", "Convertible", 10000)
    print(my_vehicle.color)
    print(my_vehicle.year)
    print(my_vehicle.make)
    print(my_vehicle.model)
    print(my_vehicle.mileage)
    print(my_vehicle.honk())
    print(my_vehicle.drive(1234))
    print(my_vehicle.num_wheels)
    print(my_vehicle.style)
    print(my_vehicle.top_open)
    print(my_vehicle.lower_roof)
    print(my_vehicle.raise_roof)
