n = int(input("Enter the number of elements: "))
list1 = []
for i in range(n):
    x = input("Enter element : ")
    list1.append(x)
reversed = list1[::-1]
print("Reversed list:", reversed)
