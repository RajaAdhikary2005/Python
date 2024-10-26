num = int(input("Enter a number: "))
num2 = num
num3 = num
count = 0
arm = 0
count=len(str(num))

for i in range(0, count):
    rem = num2 % 10
    arm += rem ** count
    num2 //= 10

if arm == num3:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
