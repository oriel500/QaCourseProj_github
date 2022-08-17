from random import randint

num = randint(1, 9)
guss_num = int(input("Guss the number between 1 util 9: "))

while num != guss_num:
    if num < guss_num:
        guss_num = int(input("The guss higher from the number, Try again: "))
    elif num > guss_num:
        guss_num = int(input("The guss lower from the number, Try again: "))

print("Your guss is right!")