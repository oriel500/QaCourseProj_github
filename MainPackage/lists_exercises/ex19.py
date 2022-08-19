from random import randint

list1 = [randint(1, 10) for i in range(10)]
list_temp = list1.copy()
print(list1)

for digit in list1:
    if list_temp.count(digit) != 0:
        print(f"You have {list_temp.count(digit)} times the digit {digit}")

    # remove the digit from the list
    while digit in list_temp:
        list_temp.remove(digit)
