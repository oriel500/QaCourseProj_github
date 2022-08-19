word = input()
list1 = []
for index in range(len(word)):
    if  word[index] not in word[index+1:]:
        list1.append(word[index])

print(list1)