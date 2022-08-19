number = int(input("Enter number: "))
list1 = []
for i in range(101):
    if i+1 < number and number % (i+1) == 0:
            list1.append(i+1)
    elif i+1 > number and (i+1) % number == 0:
            list1.append(i+1)

print(list1)
