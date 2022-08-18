string = input("Enter string: ")
char = input("Enter cahr: ")
count = 0

for letter in string:
    if letter == char:
        count += 1

print(string.count(char))
print(count)