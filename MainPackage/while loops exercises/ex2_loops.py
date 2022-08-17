age = int(input("Enter age: "))

while 0 <= age <= 120:
    if 0 <= age <= 18:
        print("child")
    elif 16 <= age <= 60:
        print("adult")
    else:
        print("senior")
    age = int(input("Enter age: "))

print("invalid")