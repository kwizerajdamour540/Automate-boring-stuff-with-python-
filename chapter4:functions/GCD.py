def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# Example
x=int(input("enter number 1:"))
y=int(input("enter number 2:"))
print(f"GCD of {x}  and {y}:", gcd(x, y))
