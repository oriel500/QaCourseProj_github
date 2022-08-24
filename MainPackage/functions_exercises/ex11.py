def create_list_double(list_):
    for i in range(2, 41):
        if i % 2 == 0:
            list_.append(i)
    return list_


# == maim ==
list1 = []
list1 = create_list_double(list1)
print(list1)
