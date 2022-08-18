arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# just 3 index from the end
# print backward
new_arr = arr[7:]
print(new_arr[::-1])

# a even index list : indexes 2,4,6,8
new_arr = arr.copy()
print(new_arr[2::2])

# a odd list
print(arr[::2])

# change index 4,5, and the index in the end
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
new_arr = arr.copy()
new_arr[4] = num1
new_arr[5] = num2
new_arr[-1] = num3
print(new_arr)

# create a list with the values in arr but double 2
new_arr = []
for i in arr:
    new_arr.append(i*2)
print(new_arr)

# create a list with the final index and first index
new_arr = [arr[0], arr[-1]]
print(new_arr)