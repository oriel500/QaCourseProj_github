num = int(input("Enter number: "))
sum = 0
new_num = num

while new_num > 0:
    sum += new_num % 10
    new_num //= 10

print(sum)
