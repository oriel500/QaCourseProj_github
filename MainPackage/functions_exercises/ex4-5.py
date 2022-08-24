def sum_numbers(a):
    return sum(range(1, a+1))


# ==main==
num = int(input("enter number: "))
print(sum_numbers(num))


sum1 = 0
for i in range(5):
    num = int(input(f"enter number {i+1}: "))
    sum1 += sum_numbers(num)

print(sum1)
