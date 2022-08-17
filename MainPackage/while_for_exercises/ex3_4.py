num = int(input("Enter number:"))
min = num

while num > 0:
    if min > num:
        min = num
    num = int(input("Enter number: "))

if min > 0:
    print(min)
