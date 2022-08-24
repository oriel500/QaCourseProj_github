num = int(input("Enter number: "))

while 10 <= num <= 99:
    if (num % 7 == 0) or (num // 10 == 7) or (num % 10 == 7):
        print("Your number is lucky number!")
    else:
        print("Your number is not lucky number")
    num = int(input("Enter number: "))

print("Your number is not by 2 digits")
