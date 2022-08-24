from MainPackage.CLASSES.Car import *


def create_list_double(first=0, end=1):
    """ get number and create list until the number, return list with just double numbers """
    list_temp = []
    for i in range(first, end + 1):
        if i % 2 == 0:
            list_temp.append(i)
    return list_temp


# === main program ===
list1 = create_list_double(1, 10)
print(list1)

car = Car()
