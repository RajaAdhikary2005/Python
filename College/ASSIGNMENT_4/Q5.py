n = input("Enter a string: ")
flag = 0
left = 0
right = len(n) - 1

while left < right:
    if n[left] != n[right]:
        flag = 1
        break
    left += 1
    right -= 1

if flag == 0:
    print("Palindrome")
else:
    print("Not a palindrome")
n = input("Enter a string: ")
l = 0
d = 0
s = 0

for i in n:
    if i.isalpha():
        l += 1
    elif i.isdigit():
        d += 1
    else:
        s += 1

print("Letters:", l, "Digits:", d, "Special Symbols:", s)
