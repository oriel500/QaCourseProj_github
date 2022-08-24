sum = 0
count = 0

for i in range(6):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        sum += num
        count += 1

print(sum/count)