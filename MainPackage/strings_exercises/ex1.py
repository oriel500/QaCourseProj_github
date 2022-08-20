word = input("Enter word: ")
for letter in word:
    if letter == 'a' or letter == 'A':
        continue
    else:
        print(letter, end="")
