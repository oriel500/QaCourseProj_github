dic1 = {1: 10, 2: 20, 5: 10, 3: 30, 4: 10}
new_dic = {}


for key in dic1:
    if dic1[key] not in new_dic.values():
        new_dic[key] = dic1[key]

print(new_dic)
