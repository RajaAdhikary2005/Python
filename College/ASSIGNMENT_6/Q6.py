s=input("Enter a string: ")
words = s.split()
for i in words:
    print(i[::-1], end=' ')
