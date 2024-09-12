n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    x = int(input())
    numbers.append(x)

squared = []
for j in numbers:
    squared.append(j**2)

print("Squared list in reverse order:", squared[::-1])
