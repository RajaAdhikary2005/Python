def sum(tuple1):
    total = 0
    for i in tuple1:
        total += i
    return total

list1 = []
n = int(input("Enter the number of elements: "))

for i in range(n):
    x= int(input("Enter number: "))
    list1.append(x)

tuple1 = tuple(list1)
result = sum(tuple1)
print(f"The sum of the elements in the tuple is: {result}")
