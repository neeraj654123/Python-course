# Multilevel Inheritance

class Grandfather:
    def house(self):
        print("Grandfather's House")

class Father(Grandfather):
    # Father inherits house() from Grandfather and adds its own method car().
    def car(self):
        print("Father's Car")

# ----- Bottom class inheriting from Father (and indirectly from Grandfather) -----
class Son(Father):
    # Son inherits house() from Grandfather, car() from Father,
    # and defines its own method bike().
    def bike(self):
        print("Son's Bike")

s = Son()

s.house()   # Inherited from Grandfather (two levels up)
s.car()     # Inherited from Father (one level up)
s.bike()    # Son's own method