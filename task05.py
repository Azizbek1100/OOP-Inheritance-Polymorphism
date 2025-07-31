class Appliance:
    def turn_on(self):
        return "Appliance is now on"

    def turn_off(self):
        return "Appliance is now off"

class TV(Appliance):
    def turn_on(self):
        return "TV is now showing channels"

    def turn_off(self):
        return "TV is now off"

class Fridge(Appliance):
    def turn_on(self):
        return "Fridge is cooling"

    def turn_off(self):
        return "Fridge is turned off"

devices = [TV(), Fridge()]
for d in devices:
    print(d.turn_on())
    print(d.turn_off())