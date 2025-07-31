class Vehicle:
    def show_info(self):
        return "Generic vehicle info"

class Car(Vehicle):
    def show_info(self):
        return "This is a car with 4 wheels"

class Bike(Vehicle):
    def show_info(self):
        return "This is a bike with 2 wheels"

vehicles = [Car(), Bike()]
for v in vehicles:
    print(v.show_info())