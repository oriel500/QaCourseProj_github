fibo_count = int(input("How many fibonnaci numbers to generate: "))
list1 = [0, 1]
sum = 1

for i in range(2, fibo_count):
    list1.append(sum)
    sum += list1[i-1]
print(list1)
