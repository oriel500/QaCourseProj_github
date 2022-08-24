def tow_numbers_pow(a, b):
    if b == 0:
        return a * a
    result = tow_numbers_pow(a, b - 1)
    return result


# == main ==
num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))
print(tow_numbers_pow(num1, num2))


