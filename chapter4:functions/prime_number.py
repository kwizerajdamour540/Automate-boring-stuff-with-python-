def is_prime(n, divisor=2):
    if n <= 1:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor + 1)


# Example
x=int(input("enter first number to check if is prime:"))
print(f"Is{x} prime?", is_prime(x))

y=int(input("enter second number :"))

print(f"Is {y}  prime?", is_prime(y))

print ("funny!!!!!")
