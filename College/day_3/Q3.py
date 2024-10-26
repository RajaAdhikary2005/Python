n = int(input("Enter the number of items: "))
d = {}
for i in range(n):
    k = input("Enter key : ")
    v = input("Enter value : ")
    d[k] = v
k1 = input("Enter the key to remove: ")
if k1 in d:
    del d[k1]
    print("Updated dictionary:", d)
else:
    print("key not found")