# Taking input for a tuple
n = int(input("Enter the number of elements in the tuple: "))
list1 = []
for i in range(n):
    x = int(input(f"Enter element {i+1}: "))
    list1.append(x)

# Creating a tuple from the list
tuple1 = tuple(list1)

# Checking if an element exists in the tuple
element = int(input("Enter an element to check: "))
if element in tuple1:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")
