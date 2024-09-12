s=int(input("Enter The Starting Range: "))
e=int(input("Enter The Ending Range: "))
for i in range(s, e + 1):
     if i % 3 == 0 and i % 2==0:
        print(i)
