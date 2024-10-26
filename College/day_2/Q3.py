list1 = []
list2 = []

n1 = int(input("Enter the number of elements:  "))
for i in range(n1):
    number = int(input("Enter number for the first tuple: "))
    list1.append(number)

n2 = int(input("Enter the number of elements:  "))
for i in range(n2):
    number = int(input("Enter number for the second tuple: "))
    list2.append(number)

tuple1 = tuple(list1)
tuple2 = tuple(list2)

merge = tuple1 + tuple2

print("The merged tuple is:", merge)
