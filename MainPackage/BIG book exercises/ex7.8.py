list_names = ["Oriel", "Lidor", "Shaked", "Oded", "Michal"]
list_grades = [100, 55, 95, 81, 70]
dic1 = {}

for i in range(len(list_names)):
    dic1[list_names[i]] = list_grades[i]

#average
avg = sum(dic1.values()) / len(dic1)

#create a list of names upper to average grade
list1 = []
for key in dic1:
    if dic1[key] >= avg:
        list1.append(key)

print(dic1)
print(avg)
print(list1)
