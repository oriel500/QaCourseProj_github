length_series= int(input("Enter how many digits: "))

for i in range(length_series):
    if i == 0:
        first = 0
        print(i)
    elif i == 1:
        second = 1
        print(i)
    else:
        sum = first + second
        first = second
        second = sum
        print(sum)

