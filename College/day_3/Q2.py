n = int(input("Enter the number of items: "))
d = {}
for i in range(n):
    k = input("Enter key : ")
    v = input("Enter value : ")
    d[k] = v
k1 = input("Enter the key: ")
print("Value for the key:", d.get(k1, "Key not found"))
