# Method Overriding

class Employee:
    def working_hours(self):
        return 45

class Intern(Employee):
    def working_hours(self):    # overrides parent method
        return 40

e1=Intern()
print(e1.working_hours())