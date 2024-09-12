# Taking input for a sequence of list1
n = int(input("Enter the number of elements for the sequence tuple: "))
list1 = []
for i in range(n):
    x = int(input(f"Enter element {i+1}: "))
    list1.append(x)

# Creating a tuple from the list
tuple1= tuple(list1)
print("tuple:", tuple1)

