n = int(input("Enter the number of elements: "))
list = []

for i in range(n):
    x = int(input())
    list.append(x)

NewList = []
for i in list:
    if i not in NewList:
        NewList.append(i)
print("List after Removing duplicates:", NewList)
