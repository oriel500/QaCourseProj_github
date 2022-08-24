num = float(input("Enter number by 3 digits: "))
hun = num // 100
doz = num // 10 % 10
sin = num % 10

print(sin*100+doz*10+hun)

