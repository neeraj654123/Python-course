import json

students = {
    'student1': {'roll': 101, 'name': 'John', 'percent': 98.5,'sports':'football'},
    'student2': {'roll': 102, 'name': 'Carol', 'percent': 95.5},
    'student3': {'roll': 103, 'name': 'Alice', 'percent': 88.5}
}

print(students)
print(type(students))

# dump()

# with open("student_data.json", "x") as fh:
#     json.dump(students, fh)

# load()
# with open("student_data.json", "r") as fh:
#     data =json.load(fh)

# print(data)
# print(type(data))

# update

with open("student_data.json", "r") as fh:
    data =json.load(fh)

data.update()