n = int(input("Enter the number of elements: "))
numbers = []
for i in range(n):
    x = int(input())
    numbers.append(x)

small = numbers[0]
large= numbers[0]
for i in range(1, n):
    if numbers[i] < small:
        small = numbers[i]
for i in range(1, n):
    if numbers[i] > large:
        large = numbers[i]
print("Smallest element in the list:", small)
print("Largest element in the list:", large)
