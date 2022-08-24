def numbers_between(lower=1, top=1):
    for i in range(lower, top + 1):
        print(i, end=" ")


def bigger(a, b):
    if a >= b:
        return a
    return b


def smaller(a, b):
    if a <= b:
        return a
    return b


# == main ==
num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))
numbers_between(smaller(num1, num2), bigger(num1, num2))
