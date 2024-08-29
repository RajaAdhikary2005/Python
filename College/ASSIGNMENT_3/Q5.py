start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(f"Prime numbers between {start} and {end}:")
for num in range(start, end + 1):
    if num > 1:  
        flag = 0
        for i in range(2, num):  
            if num % i == 0:
                flag = 1
                break
        if flag == 0: 
            print(num)
