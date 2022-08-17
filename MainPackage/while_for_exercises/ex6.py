grade = float(input("Enter grade:"))
count_pass = 0
sum_pass = 0
count_fail = 0
sum_fail = 0

while 0 <= grade <= 100:
    if grade >= 60:
        sum_pass += grade
        count_pass += 1
    else:
        sum_fail += grade
        count_fail += 1

    if count_pass != 0:
        print("The average grades pass is: ", sum_pass / count_pass)
    if count_fail != 0:
        print("The average grades failed is: ", sum_fail / count_fail)
    grade = float(input("Enter grade again:"))


print("invalid")
