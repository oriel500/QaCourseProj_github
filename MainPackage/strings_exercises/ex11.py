word = input("Enter word: ")
sentence = input("Enter sentence: ")
list1 = sentence.split()
list2 = []

for index in range(len(list1)):
    if list1[index] == word:
        list2.append(index)

print(list2)