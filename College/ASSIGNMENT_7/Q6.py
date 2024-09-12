n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    x = int(input())
    numbers.append(x)

if n == 0:
    print("The list is empty.")
else:
    print("The list is not empty.")
