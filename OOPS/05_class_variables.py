# Class Variables

class student:
    college_name="ABC"                                   # Class Variables
    depatments=["Arts","Commerce","Science"]             # Class Variables
    def __init__(self,name):                             
        self.name=name                       
        print("self.n=",self.n)
s = student("John")
print(s.college_name) 
print(s.depatments)
# help(student)