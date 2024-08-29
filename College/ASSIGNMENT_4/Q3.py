n = int(input("Enter a number: "))
divisor = 0

for i in range(1, n):
    if n % i == 0:
        divisor += i

if divisor == n:
    print("It is a perfect number")
else:
    print("It is not a perfect number")
