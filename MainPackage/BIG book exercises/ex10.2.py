def sum_numbers (*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(sum_numbers(7, 0, 3, 2, 8))