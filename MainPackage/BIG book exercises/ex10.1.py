def max_numbers(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    return c


print(max_numbers(4, 1, 2))
