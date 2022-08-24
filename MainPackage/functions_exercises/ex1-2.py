def sum_3_digits(num):
    a100 = num // 100
    a10 = (num // 10) % 10
    a1 = num % 10
    return a100 + a10 + a1


def is_valid_3_digits(num):
    if 100 <= num <= 999:
        return True
    else:
        return False


num = int(input("enter number: "))
while not is_valid_3_digits(num):
    num = int(input("enter number again: "))

print(sum_3_digits(num))
