list1 = []
n = int(input("Enter the number of elements: "))

for i in range(n):
    x = int(input("Enter element : "))
    list1.append(x)

ascending = sorted(list1)
descending = sorted(list1, reverse=True)

print("Sorted in ascending order:", ascending)
print("Sorted in descending order:", descending)
