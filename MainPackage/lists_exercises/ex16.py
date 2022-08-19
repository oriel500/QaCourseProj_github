list1 = [1, 2, 3, 3, 4, 5, 5]
list2 = []
for i in range(len(list1)):
    if list1[i] not in list1[i+1:]:
        list2.append(list1[i])

print(list2)
