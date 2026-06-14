#Initializer (__init__)

class student:
    def __init__(self,n):                    #Initializer
        print("calling initializer")
        self.n=n                          #Instance Variable
        print("self.n=",self.n)
s = student(10)
# print(s.n)       
