n = int(input("Enter the number of elements for the tuple: "))
list1 = []
for i in range(n):
    x = input("Enter element : ")
    list1.append(x)
list1[0],list1[-1]=list1[-1],list1[0]
t = tuple(list1)
print("Swapped tuple:", t)
