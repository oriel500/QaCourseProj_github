def kind_age(age1):
    if 0 <= age1 <= 18:
        return "child"
    elif 19 <= age1 <= 60:
        return "adult"
    elif 61 <= age1 <= 120:
        return "senior"
    else:
        return "invalid"


#== main ==
for i in range(5):
    age = int(input(f"enter age {i+1}: "))
    print(kind_age(age))
