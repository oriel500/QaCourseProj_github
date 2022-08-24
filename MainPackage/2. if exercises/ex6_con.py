grade = int(input("enter grade: "))

if 0 <= grade <= 100:
    if grade >= 70:
        print("pass")
    else:
        print("fail")
else:
    print("invalid grade")