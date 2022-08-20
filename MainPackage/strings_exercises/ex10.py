from random import randint
name = input("Enter name: ")
password = ""

for i in range(6):
    password += name[randint(0, len(name)-1)]

print(password)
