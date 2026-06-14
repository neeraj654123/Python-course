import pickle
students ={'student1': {'roll': 101, 'name': 'John', 'percent': 78.5},
           'student2': {'roll': 102, 'name': 'Carol', 'percent': 88.5},
           'student3': {'roll': 103, 'name': 'Serina', 'percent': 98.5}}
print(students, type(students))

# Serialization
with open("students.bin", "wb") as fh:
    for student in students:
        pickle.dump(students[student], fh)

# Deserialization
student_list90 =[]
with open("students.bin", "rb") as fh:
    while True:
        try:   
            data = pickle.load(fh)
            if data['percent'] >=90:
                student_list90.append(data['name'])
        except EOFError:
            print("Done")
            break

print(student_list90)