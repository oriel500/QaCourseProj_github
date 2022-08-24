sentence = input("Enter sentence: ")
word = input("Enter word: ")
# i am learning python and i am not learning java and i am amazed

list1 = []
start_index = 0

for i in range(sentence.count(word)):
    fount_index = sentence.index(word, start_index)
    list1.append(fount_index)
    start_index = fount_index + 1

print(list1)
