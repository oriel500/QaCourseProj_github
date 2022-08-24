dic1 = {1: 10, 2: 20, 3: 30}
dic2 = {}

for key in dic1:
    dic2[dic1[key]] = key

print(dic2)
