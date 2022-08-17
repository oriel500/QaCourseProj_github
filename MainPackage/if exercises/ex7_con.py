number = int(input("enter number by 2 digits: "))

if 10 <= number <= 99:
    if (number % 10 == 7 or number // 10) or number % 7 == 0:
        print("Lucky number")
else:
    print("invalid number")
