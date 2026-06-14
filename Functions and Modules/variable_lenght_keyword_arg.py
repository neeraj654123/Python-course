# **kwargs - variable length keyword arguments

def student_details(sid, sname, *extra, **marks):
    if len(marks) == 0:
        print(f"{sname} did not attend the exam")
    else:
        percent = sum(marks.values()) / len(marks)
        print(f"{sname} with id {sid} secured {percent}%")

    print(f"{sname} does {extra}")


student_details(101,"John",'football', sub1=78.5, sub2=81.0)
student_details(102,"Carol","tennis , debates", sub4=78.0)