from random import randint

# number between 0-100
num = int(input("Think about number between 0 until 100: "))
count = 1
min = 0
max = 100

# the system guss number between 0 - 100
guss_number = randint(min, max)
print(f"The computer guss the number {guss_number}")

while guss_number != num:
    count += 1
    user_intent = input("Write lower or higher: ")
    if user_intent == "lower":
        min = guss_number
        guss_number = randint(min, max)
    elif user_intent == "higher":
        max = guss_number
        guss_number = randint(min, max)

    print(f"The computer guss the number {guss_number}")

print(f"The computer guss the number after {count} tries")
