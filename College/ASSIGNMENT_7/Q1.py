n = int(input("Enter the number of elements: "))
numbers = []
for i in range(n):
    x = int(input())
    numbers.append(x)   
sum = 0

for i in numbers:
    sum += i

print("Sum of the list:", sum)
