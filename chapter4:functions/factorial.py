def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Example
x=int (input("enter number to display its factorial:"))

print("Factorial of 5:", factorial(x))
