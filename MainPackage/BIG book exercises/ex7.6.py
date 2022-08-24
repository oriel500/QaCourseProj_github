dic1 = {1: 10, 2: 20, 3: 30}
key_remove = int(input("Enter key as integer: "))

if key_remove in dic1:
    del dic1[key_remove]

print(dic1)