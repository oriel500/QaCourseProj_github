sentence = input("Enter sentence: ")
letter1 = input("Enter letter: ")
new_sentence = ""

"""for letter in sentence:
    if letter1 == letter:
        new_sentence += letter.capitalize()
    else:
        new_sentence += letter"""

sentence = sentence.replace(letter1, letter1.capitalize())
print(sentence)
