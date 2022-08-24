num = int(input("Enter number by 3 digits"))

if 100 <= num <= 999:
    sum = (num // 100) + (num // 10 % 10) + (num % 10)
    print(sum)
else:
    print("invalid number!")