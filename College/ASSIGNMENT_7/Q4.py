n = int(input("Enter the number of strings: "))
strings = []

for i in range(n):
    s = input()
    strings.append(s)

count = 0
for s in strings:
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1

print("Count of strings with same first and last characters:", count)
