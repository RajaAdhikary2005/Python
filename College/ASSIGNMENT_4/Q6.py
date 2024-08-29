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
