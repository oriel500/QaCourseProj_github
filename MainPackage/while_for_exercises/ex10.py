num = int(input("Enter number: "))
count = 0

while num != 0:
    if num % 7 == 0 or num % 3 == 0:
        count += 1
    num = int(input("Enter number: "))

print(count)
