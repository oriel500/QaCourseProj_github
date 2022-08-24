def is_range (num, low, top):
    if low <= num <= top:
        return True
    return False


print(is_range(100, 0, 99))
