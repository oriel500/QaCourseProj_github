word = input("Enter word: ")
letter = input("Enter letter: ")
count = 0

for i in word:
    if i == letter:
        count += 1

print(count)