grade = float(input("Enter grade:"))
count = 0
max = 0
sum = 0
avg = 0

while 0 <= grade <= 100:
    count += 1
    if grade > max:
        max = grade

    sum += grade
    grade = float(input("Enter grade:"))

if count != 0:
    avg = sum / count
print("max number: ", max)
print("avarage: ", avg)
print("different: ", max - avg)
