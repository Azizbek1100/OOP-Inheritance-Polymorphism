class Product:
    def get_delivery_method(self):
        return "Delivery method varies"

class PhysicalProduct(Product):
    def get_delivery_method(self):
        return "Ships via courier"

class DigitalProduct(Product):
    def download(self):
        return "Download link sent to email"

items = [PhysicalProduct(), DigitalProduct()]
for item in items:
    print(item.get_delivery_method())
    if isinstance(item, DigitalProduct):
        print(item.download())