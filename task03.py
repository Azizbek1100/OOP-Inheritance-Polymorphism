class User:
    def access_level(self):
        return "Basic access"

class Admin(User):
    def access_level(self):
        return "Full access"

class Guest(User):
    def access_level(self):
        return "Read-only access"

users = [Admin(), Guest()]
for u in users:
    print(u.access_level())