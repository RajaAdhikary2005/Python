# Taking input for a list
n = int(input("Enter the number of elements in the list: "))
numbers = []
for i in range(n):
    x = int(input(f"Enter element {i+1}: "))
    numbers.append(x)

# Taking input for elements to remove
remove_count = int(input("How many elements to remove: "))
for i in range(remove_count):
    element = int(input(f"Enter element {i+1} to remove: "))
    if element in numbers:
        numbers.remove(element)

# Printing the list after removal
print("List after removing elements:", numbers)
