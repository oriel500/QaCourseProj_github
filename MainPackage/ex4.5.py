length = int(input("How many gardes you want: "))
below60 = []
above60 = []

for i in range(length):
    grade = float(input(f"Enter your grade {i+1}: "))
    # check if the grade valid
    while grade > 100 or grade < 0:
        grade = float(input(f"invalid!, Enter your grade {i+1} again: "))

    if grade <= 60:
        below60.append(grade)
    elif grade > 60:
        above60.append(grade)

print(len(above60), " grades pass")
print(len(below60), " grades failed")

