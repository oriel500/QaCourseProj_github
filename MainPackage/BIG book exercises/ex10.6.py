def count_upper_lower_letter (word):
    count_upper = 0
    count_lower = 0
    if type(word) is str:
        for letter in word:
            if letter.isupper():
                count_upper += 1
            elif letter.islower():
                count_lower += 1
        print(f"count upper: {count_upper}, count lower: {count_lower}")
    else:
        print("invalid")


count_upper_lower_letter("WorD")