string = input("Enter string: ")
char = input("Enter char: ")
count = 0

for letter in string:
    if letter == char:
        count += 1

print(count)
# print(string.count(char))
