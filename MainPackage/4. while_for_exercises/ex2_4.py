num = int(input("Enter number:"))
count = 0
new_num = num

while new_num > 0:
    count += 1
    new_num //= 10

print(count)