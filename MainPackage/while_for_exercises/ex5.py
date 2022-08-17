grade = float(input("Enter grade:"))
count = 0
sum = 0

while 0 <= grade <= 100:
    if grade >= 60:
        sum += grade
        count += 1

    print("The avarage grades pass is: ", sum / count)
    grade = float(input("Enter grade again:"))

print("invalid")