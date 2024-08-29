import math

# Input sides of the triangle
a = int(input("Enter the first side of the triangle: "))
b = int(input("Enter the second side of the triangle: "))
c = int(input("Enter the third side of the triangle: "))

# Calculate the semi-perimeter
s = (a + b + c)/2

# Calculate the area using Heron's formula
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("The area of the triangle is: ",area)
