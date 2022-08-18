from random import randint
list1 = []

for i in range(10):
    list1.append(randint(0, 100))
tup1 = (*list1,)
print(tup1)

num = int(input("Enter number: "))
tup1 += (num,)
print(tup1)

tup1 = (*list1,)
tup2 = tup1[0:4] + tup1[6:]
print(tup2)

tup3 = tup2[1:]
print(tup3)
