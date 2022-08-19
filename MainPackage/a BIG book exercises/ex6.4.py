from random import randint
list1 = []

# 10 random number between 0-100 to list1
for i in range(10):
    list1.append(randint(0, 100))

# list to tuple
tup1 = ()
for i in list1:
    tup1 += (i,)
print(tup1)

# add num to tuple
num = int(input("Enter number: "))
tup1 += (num,)
print(tup1)

# list to tuple again and print 4 first index and last
tup1 = ()
for i in list1:
    tup1 += (i,)
tup2 = tup1[:4] + tup1[-4:]
print(tup2)

# print remove first index from tup2
tup3 = tup2[1:]
print(tup3)
