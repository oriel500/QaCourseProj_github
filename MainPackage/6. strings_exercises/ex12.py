sentence = input("Enter sentence: ")
list1 = sentence.split()

for i in range(len(list1)):
    list1[i] = list1[i].capitalize()
sentence = " ".join(list1)
print(sentence)