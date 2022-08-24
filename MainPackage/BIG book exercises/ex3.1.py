num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

for i in range(num1+1, num2):
    if i % 2 == 0:
        print(i)