n = int(input("Enter the number of items: "))
d = {}
for i in range(n):
    k = input("Enter key : ")
    v = input("Enter value : ")
    d[k] = v
print("Dictionary:", d)
