def sum_double_numbers(list1):
    sum = 0
    for i in list1:
        if i % 2 == 0:
            sum += i
    return sum


print(sum_double_numbers([1, 2, 3, 4, 5, 6]))
