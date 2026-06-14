# Abstract Class - Usage

from my_abstract_class import shape

class Rectangle(shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    # def area(self):
    #     return self.l * self.b

r = Rectangle(5, 6)
# print(r.area())    # Output: 30 