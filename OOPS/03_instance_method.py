#instance method

class Student:
    '''if no self,Python will raise an error when you call it using an object.It automatically 
    passes the object (s1) as the first argument. Since display()expects 0 arguments'''
    def display(self,n_hours):  
        print(f"The student studies for {n_hours} hours")  
s1 = Student()
s1.display(5)   
   