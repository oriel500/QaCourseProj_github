num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if num1 > num2 and num1 > num3:
    print(f"num1: {num1} is the bigest")
elif num2 > num1 and num2 > num3:
    print(f"num2: {num2} is the bigest")
elif num3 > num1 and num3 > num2:
    print(f"num3: {num3} is the bigest")
else:
    print("All the number euqels")