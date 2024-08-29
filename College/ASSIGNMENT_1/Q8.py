principal = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest: "))
time = int(input("Enter the time (in years): "))

simple_interest = (principal * rate_of_interest * time) / 100
print("The simple interest is: ",simple_interest)
