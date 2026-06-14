def add(num1):
    return num1 +1

def square(num1):
    return num1**2

num =int(input("Enter a no.: "))
res =square(add((num)))
print(f"output is: {res}")