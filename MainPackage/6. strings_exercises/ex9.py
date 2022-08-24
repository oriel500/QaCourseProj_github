word1 = input("Enter word: ")
word2 = input("Enter word 2: ")
eq_letter = []

for i in word1:
    if i in word2 and i not in eq_letter:
        eq_letter.append(i)

print(*eq_letter)
print(len(eq_letter))
