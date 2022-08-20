word = input("Enter word: ")
letter = input("Enter letter: ")

if letter not in word:
    print(-1)
else:
    for i in range(len(word)):
        if word[i] == letter:
            print(i)
            break

