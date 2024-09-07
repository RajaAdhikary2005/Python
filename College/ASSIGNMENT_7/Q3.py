n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    x = int(input())
    numbers.append(x)
temp = numbers[0]
numbers[0] = numbers[-1]
numbers[-1] = temp

print("List after interchanging first and last elements:", numbers)
