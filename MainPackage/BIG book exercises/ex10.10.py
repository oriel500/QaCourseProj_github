def is_falindrom(word):
    temp_word = word
    if " " in word:
        list_word = word.split()
        temp_word = "".join(list_word)
    if temp_word == temp_word[::-1]:
        return True
    return False


print(is_falindrom("nurses run"))
print(is_falindrom("Oriel"))
