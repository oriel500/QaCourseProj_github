word1 = input("Enter word: ")
word2 = input("Enter word 2: ")
eq_letter = []
count = 0

for i in range(len(word1)):
    for y in range(len(word2)):
        if (word1[i] == word2[y]) and (word2[y] not in eq_letter):
            count += 1
            eq_letter.append(word2[y])
print(count)
