from random import randint

# number between 0-100
input("Think of a number between 0-100... press enter you are ready")
count = 0
min = 0
max = 100

# the system guss number between 0 - 100
guss_number = randint(min, max)
print(f"The computer guss the number {guss_number}")

user_intent = input("Write lower or higher or correct: ")
while user_intent != "correct":
    count += 1
    if user_intent == "lower":
        min = guss_number
        guss_number = randint(min, max)
    elif user_intent == "higher":
        max = guss_number
        guss_number = randint(min, max)

    print(f"The computer guss the number {guss_number}")
    user_intent = input("Write lower or higher or correct: ")

print(f"The computer guss the number after {count} tries")
