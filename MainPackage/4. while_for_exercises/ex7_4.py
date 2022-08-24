num1 = int(input("Eenter number 1: "))
num2 = int(input("Eenter number 2: "))
count = 0

if num1 > 0 and 0 < num2 <= num1:
    while num1 >= num2:
        num1 -= num2
        count += 1

    print("number1 / number 2 = ", count)
    print("number1 % number 2 = ", num1)
else:
    print("One of the number invalid")
