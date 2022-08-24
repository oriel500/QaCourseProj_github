word = input("Enter word: ")
new_word = ""

for i in range(len(word)):
    if word[i] in word[i+1:]:
        new_word += word[i]

print(new_word)
