age = int(input("Enter the age: "))

if age >= 0 and age <= 12:
    print("Age category: Child")
elif age >= 13 and age <= 19:
    print("Age category: Teen")
elif age >= 20 and age <= 64:
    print("Age category: Adult")
elif age >= 65:
    print("Age category: Senior")
else:
    print("Invalid age")
