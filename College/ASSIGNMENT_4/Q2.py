n = int(input("Enter a number: "))
n_str = str(n)
sum = 0

for i in n_str:
    sum += int(i)

print("Sum of digits:", sum)
