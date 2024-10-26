n = int(input("Enter the number of elements: "))
list1 = []
for i in range(n):
    x = input("Enter element : ")
    list1.append(x)
item = input("Enter the item to add: ")
list1.append(item)
print("New list:", list1)
