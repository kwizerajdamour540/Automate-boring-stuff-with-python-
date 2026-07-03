import copy

# Original nested list
original = [["Apple", "Banana"], ["Mango", "Orange"]]

# Create copies
shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)

print("Before modification")
print("Original      :", original)
print("Shallow Copy  :", shallow_copy)
print("Deep Copy     :", deep_copy)

# Modify the first inner list in the shallow copy
shallow_copy[0][0] = "Pineapple"

# Modify the first inner list in the deep copy
deep_copy[1][1] = "Grapes"

print("\nAfter modification")
print("Original      :", original)
print("Shallow Copy  :", shallow_copy)
print("Deep Copy     :", deep_copy)
