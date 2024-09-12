n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    x = int(input())
    numbers.append(x)

k = int(input("Enter the value of k: "))
print(f"Elements with count greater than {k} and their frequency:")
for i in set(numbers):
    count = numbers.count(i)
    if count > k:
        print(f"Element {i}: Frequency {count}")
