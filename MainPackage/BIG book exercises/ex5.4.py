sentence = input()

# length of sentence
print(len(sentence))

# return 4 letters from letter 3 until letter 6
print(sentence[3:6])

# return the first word 3 times
arr = sentence.split()
for i in range(3):
    print(arr[0])

# return the sentence when every first letter in every word will be capital
new_sentence = ""
for word in arr:
    new_sentence += word.capitalize() + " "
print(new_sentence)