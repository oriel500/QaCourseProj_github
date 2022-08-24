num = int(input("enter number by 3 digits: "))

while 100 <= num <= 999:
    a = num // 100
    b = num // 10 % 10
    c = num % 10
    print(a+b+c)
    num = int(input("enter number by 3 digits: "))

print("invalid")
