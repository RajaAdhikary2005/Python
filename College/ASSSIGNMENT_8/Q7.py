# Taking input for a list
n = int(input("Enter the number of elements in the list: "))
list1 = []
for i in range(n):
    x = int(input(f"Enter element {i+1}: "))
    list1.append(x)

# Swapping the first and last items using a tuple
list1[0], list1[-1] = list1[-1], list1[0]
print("List after swapping first and last elements:", list1)
