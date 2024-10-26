n1 = int(input("Enter the number of elements for the first tuple: "))
list1 = []
for i in range(n1):
    x = input("Enter xent  for the first tuple: ")
    list1.append(x)
t1 = tuple(list1) 

n2 = int(input("Enter the number of elements for the second tuple: "))
list2 = []
for i in range(n2):
    x = input("Enter element for the second tuple: ")
    list2.append(x)
t2 = tuple(list2) 

new = t1 + t2
print("Combined tuple:", new)
