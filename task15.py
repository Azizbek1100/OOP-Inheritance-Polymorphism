class Character:
    def attack(self):
        return "Character attacks"

    def defend(self):
        return "Character defends"

class Warrior(Character):
    def attack(self):
        return "Warrior slashes with sword"

    def defend(self):
        return "Warrior blocks with shield"

class Mage(Character):
    def attack(self):
        return "Mage casts fireball"

    def defend(self):
        return "Mage uses magic barrier"

class Archer(Character):
    def attack(self):
        return "Archer shoots an arrow"

    def defend(self):
        return "Archer dodges swiftly"

fighters = [Warrior(), Mage(), Archer()]
for f in fighters:
    print(f.attack(), "|", f.defend())