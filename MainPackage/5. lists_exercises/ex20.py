from random import randint

list1 = [randint(0, 10) for i in range(10)]
print(list1)

num = int(input("Enter number: "))
for index in range(len(list1)):
    if list1[index] == num:
        break

print(index)
