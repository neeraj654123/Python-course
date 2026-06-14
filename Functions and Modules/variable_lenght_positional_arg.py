# *args - variable length positional arguments (0 to n)

def student_details(sid, sname, *marks):
    if len(marks) == 0:
        print(f"{sname} with id {sid} was absent in all the exams!")
    else:
        percent = sum(marks) / len(marks)
        print(f"{sname} with id {sid} secured {percent}%")

student_details(101, "John", 87.0, 69.5, 81.5, 74.0)
student_details(102, "Carol", 91.0, 49.5, 91.5, 84.0, 86.5)
student_details(103, "Mark", 81.5, 83.5, 79.0)
student_details(104, "Alice")