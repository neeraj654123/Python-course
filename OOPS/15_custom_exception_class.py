# Custom Exception Class

class AgeError(Exception):
    pass

age = int(input("Enter Age: "))

if age < 18:
    raise AgeError("You must be 18 or older")

print("Eligible for voting")