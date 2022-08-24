# Create list between 1-10
list1 = []
for i in range(10):
    list1.append(i+1)
# ex5
# only even index
print(list1[0::2])

# ex6
# first 5 numbers
print(list1[:5])

# ex7
# only odd numbers
print(list1[0:-1:2])

# ex8
num = int(input("Enter number:"))
list2 = list1.copy()
list2.insert(8, num)
print(list2)

# ex9
num = int(input("Enter number:"))
list2 = list1.copy()
list2.insert(-2, num)
print(list2)

# ex10
list2 = list1.copy()
for i in list2:
    if i % 3 == 0:
        list2.remove(i)
print(list2)

# ex 11
# value 1 in index 0 and 1
list2 = []
list2.append(1)
list2.append(1)
sum = 2

for i in range(2, 10):
    list2.append(sum)
    sum += list2[i]

print(list2)
