list1 = []
n = int(input("Enter the number of eleemnt: "))

for i in range(n):
    x = input("Enter element : ")
    list1.append(x)

search = input("Enter the element to find the index of: ")

if search in list1:
    i = list1.index(search)
    print(f"The index of '{search}' is: {i+1}")
else:
    print(f"'{search}' is not in the list.")
