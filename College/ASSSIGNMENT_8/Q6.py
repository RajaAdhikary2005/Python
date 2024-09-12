# Taking input for a tuple
n = int(input("Enter the number of elements in the tuple: "))
numbers = []
for i in range(n):
    x = int(input(f"Enter element {i+1}: "))
    numbers.append(x)

# Creating a tuple from the list
tuple1 = tuple(numbers)

# Finding the length of the tuple
length = len(tuple1)
print(f"Length of the tuple: {length}")
