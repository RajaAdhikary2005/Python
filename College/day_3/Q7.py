n = int(input("Enter the number of elements : "))
list1 = []
for i in range(n):
    x = input("Enter element : ")
    list1.append(x)
item = input("Enter the item to remove: ")
if item in list1:
    list1.remove(item)
    print("Updated list:", list1)
else:
    print("Item not found in the list")
