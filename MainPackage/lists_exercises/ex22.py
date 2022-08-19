# Hang Man Program
from random import randint

# Bank of 30 words
bank = ("thor", "hulk", "iron-man", "spider-man", "hawkeye", "black-widow", "captain-america", "captain-marvel", "ant-man", "scarlet-witch",
        "falcon", "doctor-srange", "groot", "vision", "star-Lord", "gamora", "deadpool", "daredevil", "black-panther", "thanos",
         "loki", "nick-fury", "galactus", "odin", "magneto", "quicksilver", "ultron", "ms-marvel", "doctor-doom", "black-bolt")

# Input to "word" random word
word = bank[randint(0, len(bank)-1)]

# Print _ instead letters
answer = []
for letter in word:
    if letter == '-':
        answer.append('-')
    else:
        answer.append('_')
print(*answer)

# The player guss 8 tries
is_won = False
try_count = 8
while try_count > 0 and not is_won:
    guss_letter = input(f"You have {try_count} tries, Guss a letter: ")
    # if the input above 1 length or " "
    while len(guss_letter) > 1 or guss_letter[0] == " ":
        guss_letter = input("Invalid letter, try again: ")
    # if the input 1 length
    else:
        if guss_letter not in word:
            try_count -= 1
            print(*answer)
            continue

        for index in range(len(word)):
            if word[index] == guss_letter:
                answer[index] = guss_letter
        print(*answer)

        if '_' not in answer:
            is_won = True

# won or loose
if is_won:
    print("You won!")
else:
    print("You loose")
    print(f"The word is {word}")
