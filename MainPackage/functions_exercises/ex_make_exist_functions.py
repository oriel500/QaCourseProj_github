def len_list(list1: list):
    list_temp = list1.copy()
    count = 0
    while list_temp:
        count += 1
        list_temp.pop()
    return count


def count_list(list1: list, num: float):
    count = 0
    for i in list1:
        if i == num:
            count += 1
    return count


def find(list1: list, num: float, start_index: int):
    for i in range(start_index,len(list1)):
        if list1[i] == num:
            return i


def max_list(list1: list):
    max1 = 0
    for i in list1:
        if max1 < i:
            max1 = i
    return max1


def change_to_list(x):
    list1 = []
    if type(x) is (dict or str or set or tuple):
        for i in x:
            list1.append(i)
        return list1
    else:
        print("invalid argument")
        return


def remove_list(list1: list, val):
    if val not in list1:
        print("not exist")
    else:
        index = list1.index(val)
        list1.pop()
        for i in range(index, len(list1)-1):
            list1[index] = list1[index+1]


def keys_dict(dic1: dict):
    list1 = []
    for key in dic1:
        list1.append(key)
    return list1


def values_dict(dic1: dict):
    list1 = []
    for key in dic1:
        list1.append(dic1[key])
    return list1


def items_dict(dic1: dict):
    list1 = []
    for key in dic1:
        list1.append((key, dic1[key]))
    return list1


def change_to_set(list1: list):
    set1 = set()
    for i in list1:
        if i not in set1:
            set1.add(i)
    return set1


list2 = [1, 1, 2, 3, 3]
dict1 = {1: "oriel", 2: "lidor"}

print(len_list(list2))
print(count_list(list2, 1))
print(find(list2, 2, 2))
print(max_list(list2))
print(change_to_list(1.1))
remove_list(list2, 3)
print(list2)
print(keys_dict(dict1))
print(values_dict(dict1))
print(items_dict(dict1))
print(change_to_set(list2))

