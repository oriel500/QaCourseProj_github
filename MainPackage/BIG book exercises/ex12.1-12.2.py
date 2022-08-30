# ex12.2 - a
def number_lines_T():
    count = 0
    with open('story.txt', 'r') as file:
        for line1 in file:
            if line1[0] == 'T':
                continue
            count += 1
    return count


# ex12.2 - b
def number_of_the():
    count = 0
    with open('story.txt', 'r') as file:
        for line1 in file:
            list_line = line1.split()
            for word in list_line:
                if ("The" or "the") in word:
                    count += 1
    return count


# ex12.2 - c
def count_words():
    count = 0
    with open('story.txt', 'r') as file:
        for line1 in file:
            list_line = line1.split()
            for word in list_line:
                count += 1
    return count


# ex12.3 - a
def read_and_print():
    count = 0
    with open('story.txt', 'r') as story_file:
        while True:
            count += 1
            str_line = story_file.readline()
            print(str_line.strip())

            if not str_line:
                break
    return count


story_list = ["A boy is playing there.\n", "There is a playground.\n",
              "An airplane is in the sky.\n", "The sky is pink\n",
              "Alphabets and numbers are allowed in the password."]

with open('story.txt', 'w+') as story_file:
    story_file.writelines(story_list)

with open('story.txt', 'r+') as story_file:
    for line in story_file:
        print(line, end="")
    print("\n")

print(f"count lines without 'T': {number_lines_T()}")
print(f"count the or The: {number_of_the()}")
print(f"count words: {count_words()}")
print(f"count lines: {read_and_print()}")
