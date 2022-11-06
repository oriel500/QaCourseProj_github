def dup_lists(first, second):
    new_list = []
    first_index = 0
    for i in range(first.count(second)):
        first_index = first.index(second, first_index) + len(second)
        new_list.append(first_index-len(second))
        if first_index >= len(first):
            return new_list
    new_list.append(first_index)
    return new_list

print(dup_lists("oriel oriel or", "or"))



