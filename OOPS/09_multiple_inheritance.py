# Multiple Inheritance

# ----- Parent class #1 -----
class Father:
    def house(self):
        print("Father's House")

# ----- Parent class #2 -----
class Mother:
    def jewelry(self):
        print("Mother's Jewelry")

# ----- Child class that inherits from both Father and Mother -----
class Child(Father, Mother):
    pass

c = Child()

c.house()
c.jewelry()