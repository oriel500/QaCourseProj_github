# Course Object
from MainPackage.OBJECTS.Student import Student


class Course:
    """object holds information about the course"""

    def __init__(self, _id_course: int, _name: str, _max_of_students: int):
        self.id = _id_course
        self.name = _name
        self.subjects = {}  # key = subject, val = name of teacher
        self.students = []  # list of students in course
        self.max = _max_of_students  # max of students in the course

    def add_student(self, student: Student):
        """add student to list in course and return true if successes"""
        if len(self.students) < self.max:
            self.students.append(student)
            return True
        else:
            print("# The course is full!, the student not in the course #")
            return False

    def del_student(self, student: Student):
        """delete student from the list"""
        if student not in self.students:
            raise ValueError("the student must be in the list")

        for student_s in self.students:
            if student_s == student:
                self.students.remove(student)

    def add_factor(self, subject, factor):
        """for each student add factor to subject"""
        if subject not in self.subjects:
            raise ValueError("the subject must be in the list")

        for student in self.students:
            student.calc_factor(subject, factor)

    def average(self):
        """return list with grade average of all students"""
        list_average = []
        for student in self.students:
            list_average.append(student.average())

        return list_average

    def weak_students(self):
        """enter to tuple list of indexes of the most weak average grade in course"""
        tuple_index_min_avg_grade = ()
        # found the first weak average grade in list
        list_average = self.average()
        min_val = min(list_average)
        # if we have the same average grade we add to tuple the index
        for i in range(len(list_average)):
            if min_val == self.students[i].average():
                min_index = i
                tuple_index_min_avg_grade += (min_index,)

        return tuple_index_min_avg_grade

    def __str__(self):
        return f'id: {self.id}, name: {self.name.capitalize()}, max of students: {self.max}' \
               f'\nsubjects of course: {self.subjects}\nstudents: {self.students}'
