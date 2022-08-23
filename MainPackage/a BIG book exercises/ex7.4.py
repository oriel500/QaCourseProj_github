until_number = int(input("Enter number: "))
dic1 = {}

for i in range(until_number):
    dic1[i+1] = (i+1)*(i+1)

print(dic1)
