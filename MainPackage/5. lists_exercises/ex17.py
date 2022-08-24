list1 = [1, 2, 3, 3, 4, 5, 5]
list2 = [6, 7, 8, 9, 10, 11, 12]
common = False

for i in list1:
    if i in list2:
        common = True

if common: print("We have a common")
else: print("We don't have a common")
