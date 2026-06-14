# Class Methods

class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod                            # Access class variable
    def show_school(cls):
        print(cls.school)

    @classmethod
    def change_school(cls, school):         # Modify class variable
        cls.school = school

    @classmethod
    def show_school_by_obj(cls):            # show class variable by object
        print(cls.school)

Student.show_school()                       # Access class variable

Student.change_school("XYZ School")
Student.show_school()                       # Modify class variable

s1=Student("Neeraj")
s1.show_school_by_obj()                     # show class variable by object
