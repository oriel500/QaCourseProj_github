list1 = []
count = 0

for i in range(5):
    string1 = input("Enter a word: ")
    list1.append(string1)

for word in list1:
    if len(word) >= 4 and word[0] == word[-1]:
        count += 1

print(count)