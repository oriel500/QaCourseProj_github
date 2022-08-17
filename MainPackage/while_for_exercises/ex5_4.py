max = 0
x = 1

for i in range(7):
    num = int(input(f"Enter number {i + 1}: "))
    if max < num:
        max = num
        x = i+1


print(x)
