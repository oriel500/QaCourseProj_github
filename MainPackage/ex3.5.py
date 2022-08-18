length_series= int(input("Enter how many digits: "))
first = 0
second = 1
print(first, second, end=' ')

for i in range(length_series-2):
    sum = first + second
    first = second
    second = sum
    print(sum, end=' ')

