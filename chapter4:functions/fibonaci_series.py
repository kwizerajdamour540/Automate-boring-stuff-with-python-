def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Example (print first n  Fibonacci numbers)

x=int(input("enter number of term of fibonacci series:"))
for i in range(x):
    print(fibonacci(i), end=" ")
