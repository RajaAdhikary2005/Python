def max(tuple1):
    max = tuple1[0]
    for i in tuple1:
        if i > max:
            max = i
    return max

def min(tuple1):
    min = tuple1[0]
    for i in tuple1:
      if i < min:
         min = i
    return min

list1 = []
n = int(input("Enter the number of elements: "))

for i in range(n):
    x= int(input("Enter number: "))
    list1.append(x)

tuple1 = tuple(list1)

max= max(tuple1)
min= min(tuple1)

print(f"The maximum value is: {max}")
print(f"The minimum value is: {min}")
