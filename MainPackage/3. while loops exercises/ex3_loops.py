num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

while num1 % 2 == 0 and num2 % 2 == 0:
    print(f"sum: {num1+num2}")
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
else:
    if num1 % 2 == 0 or num2 % 2 == 0:
        print(f"double: {num1*num2}")
    else:
        print("the numbers are not even")
