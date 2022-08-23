dic1 = {1: 10, 2: 20, 5: 10, 3: 30, 4: 10}
list_keys = []
new_dic = {}


for key in dic1:
    if dic1[key] not in list_keys:
        list_keys.append(dic1[key])
        new_dic[key] = dic1[key]

print(new_dic)

