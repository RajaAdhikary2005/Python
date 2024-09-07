n1 = int(input("Enter the number of elements for the first list: "))
list1 = []

for i in range(n1):
    x = int(input())
    list1.append(x)

n2 = int(input("Enter the number of elements for the second list: "))
list2 = []

for i in range(n2):
    x = int(input())
    list2.append(x)

flag = 0
for item in list1:
    if item in list2:
        flag = 1
        break

if flag == 1:
    print("The lists have at least one common element.")
else:
    print("The lists do not have any common elements.")
