# Data Type Testing Module

print(type(42))               # Integer
print(type(3.14))             # Float
print(type("Hello, World!"))  # String
print(type(True))             # Boolean
print(type([1, 2, 3]))       # List
print(type((1, 2, 3)))       # Tuple
print(type({1: 'a', 2: 'b'})) # Dictionary
print(type({1, 2, 3}))       # Set


print(int("100"))          # Convert string to integer
print(float("3.14"))      # Convert string to float 
print(str(100))           # Convert integer to string
print(bool(1))            # Convert integer to boolean
print(list((1, 2, 3)))    # Convert tuple to list
print(tuple([1, 2, 3]))   # Convert list to tuple
print(dict([(1, 'a'), (2, 'b')])) # Convert list of tuples to dictionary
print(len("Hello"))        # Length of string
print(len([1, 2, 3, 4]))   # Length of list
print(sum([1, 2, 3, 4]))   # Sum of list elements
print(max([1, 2, 3, 4]))   # Maximum value in list
print(min([1, 2, 3, 4]))   # Minimum value in list
print(sorted([3, 1, 4, 2])) # Sorted list
print("Hello".upper())      # Convert string to uppercase
print("WORLD".lower())      # Convert string to lowercase
print("  Trim  ".strip())   # Trim whitespace from string