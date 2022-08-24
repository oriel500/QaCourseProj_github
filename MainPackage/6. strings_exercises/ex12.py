sentence = input("Enter sentence: ")
list1 = sentence.split()
sentence = ""

for word in list1:
    sentence += word.capitalize()
    sentence += " "

print(sentence)