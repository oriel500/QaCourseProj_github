arr1 = []
arr2 = []

for i in range(3):
    x = input("Enter to array 1: ")
    arr1.append(x)

for i in range(3):
    x = input("Enter to array 2: ")
    arr1.append(x)

arr1 += arr2
print(arr1)
print("The length of new array is ", len(arr1))