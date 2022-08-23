word = input("Enter word: ")
letter = input("Enter letter: ")

for i in range(len(word)):
    if word[i] == letter:
        print(i)
        break
else:
    print(-1)
