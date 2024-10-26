string = []
n = int(input("How many strings will you enter "))

for i in range(n):
    x = input(f"Enter string {i+1}: ")
    string.append(x)

string = tuple(string)

longest = string[0]

for i in string:
    if len(i) > len(longest):
        longest = i

print("The longest string is:", longest)
