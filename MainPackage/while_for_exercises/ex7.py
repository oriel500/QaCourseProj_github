sum = 0

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    num %= 10
    sum += num

print(sum)