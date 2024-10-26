n = int(input("Enter the number of elements: "))
list1 = []
for i in range(n):
    x = input("Enter element : ")
    list1.append(x)
t = tuple(list1)  
if len(t) > 0:
    print("First element:", t[0])
    print("Last element:", t[-1])
else:
    print("Tuple is empty")
