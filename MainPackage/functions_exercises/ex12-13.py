import random


def create_list_random(list_):
    for i in range(20):
        list_.append(random.randint(1, 100))
    return list_


def count_number(num_, list_):
    count_ = 0
    while num_ in list_:
        count_ += 1
        list_.remove(num_)
    return count_


def max_index(list_):
    return list_.index(max(list_))


# == maim ==
list1 = []
list1 = create_list_random(list1)
print(list1)

num = int(input("enter number: "))
count = count_number(num, list1.copy())
print(count)
print(list1)

print(max_index(list1))
