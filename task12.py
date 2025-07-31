class User:
    def get_dashboard(self):
        return "Generic dashboard"

class Student(User):
    def get_dashboard(self):
        return "Student dashboard: enrolled courses"

class Instructor(User):
    def get_dashboard(self):
        return "Instructor dashboard: course stats"

users = [Student(), Instructor()]
for u in users:
    print(u.get_dashboard())