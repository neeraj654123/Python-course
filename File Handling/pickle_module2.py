import pickle
students ={'student1': {'roll': 101, 'name': 'John', 'percent': 78.5},
           'student2': {'roll': 102, 'name': 'Carol', 'percent': 88.5},
           'student3': {'roll': 103, 'name': 'Serina', 'percent': 98.5}}
# print(students)
# print(type(students))

#Serialization

with open("students.bin","bw") as fh:
    for student in students:
        pickle.dump(students[student],fh)

#deserialization
with open("students.bin","rb") as fh:
    print(pickle.load(fh))
    print(pickle.load(fh))
    print(pickle.load(fh))