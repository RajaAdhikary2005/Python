s = input("Enter a string: ")
b = len(s)
count = 0

for i in range(0, b):
    if s[i] in ['a', 'e', 'i', 'o', 'u']:
        count += 1

print("Vowels:", count)
