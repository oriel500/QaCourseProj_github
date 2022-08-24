def del_common (list1):
    s1 = set(list1)
    list1 = list(s1)
    return list1


print(del_common([1, 2, 3, 3, 3, 4, 5]))