# Input details
quantity = int(input("Enter the quantity of items sold: "))
amount = int(input("Enter the value of items sold: "))
discount = int(input("Enter the discounted percentage of items sold: "))
tax = int(input("Enter the tax percentage: "))

print("**********BILL**********")
print("Quantity sold:", quantity)
print("Price per item:", amount)
print("------------------------")

# Calculate total amount, discount, and tax
total_amount = quantity * amount
discounted_amount = total_amount * (discount / 100)
discounted_total_amount = total_amount - discounted_amount
tax_amount = discounted_total_amount * (tax / 100)
total_paid = discounted_total_amount + tax_amount

# Print the bill details
print("Amount:", total_amount)
print("Discount:", discounted_amount)
print("Discounted total:", discounted_total_amount)
print("Tax:", tax_amount)
print("Total amount to be paid:", total_paid)
