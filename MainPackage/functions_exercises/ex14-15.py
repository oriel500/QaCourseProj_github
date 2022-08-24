def create_list(num_):
    list_ = []
    for i in range(num_):
        grade_ = float(input(f"enter grade {i+1}: "))
        list_.append(grade_)
    return list_


def avarage(list_):
    return sum(list_) / len(list_)


# == main ==
num_students = int(input("enter how many student do you have?: "))
list_grades = []
list_grades = create_list(num_students)
print(list_grades)
avg = avarage(list_grades)
print(avg)

