# Operator Overloading

class rectange:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b   

    def __add__(self, other):
        return self.l + other.l, self.b + other.b

r1 = rectange(5, 6)            # Rectangle with length=5, breadth=6
r2 = rectange(4, 6)            # Rectangle with length=4, breadth=6
print(r1.area())               # area of r1 → 5*6 = 30
print(r2.area())               # area of r2 → 4*6 = 24
print(r1 + r2)                 # uses __add__ → (5+4, 6+6) = (9, 12)
