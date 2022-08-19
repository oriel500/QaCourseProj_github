from random import randint
list1 = []

for i in range(20):
    list1.append(randint(0, 100))

print(list1)
number = int(input("Enter number you want remove: "))
while number in list1:
    list1.remove(number)

print(list1)