class Courier:
    def delivery_range(self):
        return 0

class BikeCourier(Courier):
    def delivery_range(self):
        return "Delivery range: 5km"

    def calculate_fee(self):
        return "$2 fee"

class CarCourier(Courier):
    def delivery_range(self):
        return "Delivery range: 20km"

    def calculate_fee(self):
        return "$5 fee"

class DroneCourier(Courier):
    def delivery_range(self):
        return "Delivery range: 10km (aerial)"

    def calculate_fee(self):
        return "$3.5 fee"

agents = [BikeCourier(), CarCourier(), DroneCourier()]
for a in agents:
    print(a.delivery_range(), "-", a.calculate_fee())