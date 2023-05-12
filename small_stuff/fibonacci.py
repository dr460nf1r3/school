# Fibonacci
# Calculate the fibonacci of the nth column

end = int(input("Enter the nth column: "))
i = 0

column = []
old = 0
new = 1
temp = 0

while i <= end:
    temp = new
    new = old
    old = temp + old
    i += 1

    column.append(old)

print(str(column).replace("[", "").replace("]", ""))
