def result(n):
    a=0
    b=0
    for i in range(3):
        a=a*10+n
        b=b+a
        if i<2:
            print(f"{a} +",end=" ")
        else:
          print(f"{a}")  
    return b
n=int(input("Enter a number: "))
num=result(n)
print(num)
    