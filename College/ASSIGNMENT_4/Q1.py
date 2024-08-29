n = int(input("Enter an integer: "))
n_str = str(n)
rev = ""

for i in range(len(n_str)-1, -1, -1):
    rev += n_str[i]

rev_n = int(rev)
print("Reversed number:", rev_n)
