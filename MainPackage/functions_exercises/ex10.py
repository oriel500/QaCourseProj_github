def is_pass(grade1):
    return 70 <= grade1 <= 100


#== main ==
for i in range(5):
    grade = int(input(f"enter grade {i+1}: "))
    while grade < 0 or grade > 100:
        grade = int(input(f"enter grade {i + 1} again: "))

    if is_pass(grade):
        print("pass")
    else:
        print("fail")
