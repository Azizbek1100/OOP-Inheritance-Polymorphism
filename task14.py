class User:
    def interact(self):
        return "General user interaction"

class Applicant(User):
    def interact(self):
        return "Applying to job positions"

class Employer(User):
    def interact(self):
        return "Posting job vacancies"

users = [Applicant(), Employer()]
for u in users:
    print(u.interact())