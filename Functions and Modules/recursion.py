"""
This module demonstrates factorial of a number using recursion.
"""

def factorial(n):
    """
    Returns the factorial of a non-negative integer using recursion.
    Parameters:
    n (int): A non-negative integer
    Returns:
    int: Factorial of n
    """
    if n == 0 or n == 1:   # Base case
        return 1
    return n * factorial(n - 1)   # Recursive case


# Driver code
num =int(input("Enter a no.: "))
print("Factorial of", num, "is", factorial(num))