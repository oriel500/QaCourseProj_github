set1 = {1, 2, 3, 4, 5}
set2 = {1, 3, 5, 6, 7}
set3 = set()

set3.update(set1)  # create set 3 with set1 and set2
set3.update(set2)
print(set3)

set3.remove(1)  # remove value
print(set3)

print(max(set3))
print(min(set3))
print(len(set3))

set4 = set3.copy()
set4.add(8)
set4.add(9)
print(set4)

set1.clear()
set2.clear()
print(f"{set1} \n{set2}")