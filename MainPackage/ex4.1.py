numbers = [] # array of numbers
sum = 0 # sum of numbers

# Build the numbers array
length = int(input("How many numbers do you want: "))
for i in range(length):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# calculate the sum
for num in numbers:
    sum += num

print(f"The max numbers is {max(numbers)}")
print(f"The avarage is {sum/length}")