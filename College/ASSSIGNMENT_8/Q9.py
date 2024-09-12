# Taking input for the first list
n = int(input("Enter the number of elements in the first list: "))
list1 = []
for i in range(n):
    x = int(input(f"Enter element {i+1} of first list: "))
    list1.append(x)

# Taking input for the second list
m = int(input("Enter the number of elements in the second list: "))
list2 = []
for i in range(m):
    x = int(input(f"Enter element {i+1} of second list: "))
    list2.append(x)

# Checking for at least one common element
flag = 0
for item in list1:
    if item in list2:
        flag = 1
        break

# Printing the result
if flag==1:
    print("The lists have at least one common element.")
else:
    print("The lists have no common elements.")
