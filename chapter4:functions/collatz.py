import sys


def collatz(number):
    if number % 2 == 0:
        # If even, floor divide by 2
        value = number // 2
    else:
        # If odd, multiply by 3 and add 1
        value = 3 * number + 1

    # Print the value on the same line with a space separating it from the next
    print(value, end=" ")
    return value


# --- Main Program Loop ---
print("Enter number:")

# Input Validation: Ensure the user inputs a valid integer
try:
    user_number = int(input())
except ValueError:
    print("Error: You must enter an integer.")
    sys.exit()

# Keep calling collatz() until the function returns 1
while user_number != 1:
    user_number = collatz(user_number)

# Print a newline at the very end to clean up the output
print()
