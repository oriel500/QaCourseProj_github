num = int(input("Enter number: "))
temp_num = num
count_dig = 0

# how many digits we have
while temp_num >= 1:
    temp_num //= 10
    count_dig += 1

# change the number to backward
right_digit = num % 10
sum = 0

while num >= 1:
    num //= 10
    for i in range(count_dig-1):
        right_digit *= 10

    sum += right_digit
    count_dig -= 1
    right_digit = num % 10

print(sum)
print(sum*2)
