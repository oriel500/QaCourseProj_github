class Course:
    def __init__(self, _num: int, _name: str, _register_students: int, _max_students: int):
        self.num = _num
        self.name = _name
        self.register_students = _register_students
        self.max_students = _max_students

    def get_max_students(self):
        return self.max_students - self.register_students

    def add_students (self, new_students: int):
        if new_students <= self.get_max_students():
            self.register_students += new_students
        else:
            #new_students -= self.self.get_max_students()
            self.register_students = self.max_students

    def __str__(self):
        return f'number: {self.num}, name: {self.name}, register: {self.register_students}, max: {self.max_students}'


# == main ==
if __name__ == "__main__":
    num_course = int(input("enter your number of course: "))
    name_course = input("enter your name of course: ")
    num_students = int(input("enter your number of students: "))
    max_students = int(input("enter your number of max students: "))
    course = Course(num_course, name_course, num_students, max_students)
    print(course)

    n = int(input("enter your number of new students: "))
    course.add_students(n)
    print(course)

