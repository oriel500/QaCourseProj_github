class Student:

    def __init__(self, _id1, _name, _grade):
        self.id1 = _id1
        self.name = _name
        self.grade = _grade

    def check_pass(self):
        if self.grade < 70:
            return False
        return True

    def update_grade(self, factor: int):
        self.grade += self.grade * (factor/100)
        if self.grade > 100:
            self.grade -= (self.grade - 100)

    def __str__(self):
        return (f'The student name is {self.name} \n'
                f'id: {self.id1}\n'
                f'grade: {self.grade}')


# == main ==
if __name__ == "__main__":
    name = input("enter student name: ")
    id1 = int(input("enter id: "))
    grade = float(input("enter grade: "))
    student = Student(id1, name, grade)

    if student.check_pass():
        print("pass")
    else:
        print("fail")

    factor1 = int(input("enter factor: "))
    student.update_grade(factor1)

    print(student)

