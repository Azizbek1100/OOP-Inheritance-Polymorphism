class Employee:
    def calculate_bonus(self):
        return 0

class Developer(Employee):
    def calculate_bonus(self):
        return "Bonus: 15% of base salary"

class Manager(Employee):
    def calculate_bonus(self):
        return "Bonus: 25% of base salary + stock options"

employees = [Developer(), Manager()]
for e in employees:
    print(e.calculate_bonus())