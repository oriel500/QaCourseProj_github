def mult_numbers (*args):
    result = 1
    for i in args:
        result *= i
    return result


print(mult_numbers(7, -1, 3, 2, 8))