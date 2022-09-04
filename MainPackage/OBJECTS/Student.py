# Student object

class Student:
    """"object holds information about student"""

    def __init__(self, _id1: int, _name: str, _age: int):
        self.id = _id1
        self.name = _name
        self.age = _age
        self.subjects = {}  # key = subject, val = grade

    def __str__(self):
        return f'id: {self.id}, name: {self.name.capitalize()}, age: {self.age}\nsubjects: {self.subjects}'

    def add_grade(self, subject: str, new_grade: float):
        """add grade to list of subjects, if the subject exist the grade update"""
        self.subjects[subject] = new_grade

    def calc_factor(self, subject, factor):
        """get subject and factor, and add to grade by the factor"""
        if subject not in self.subjects:
            raise ValueError("The subject must be exist, to add factor")

        self.subjects[subject] += self.subjects[subject] * (factor/100)
        if self.subjects[subject] > 100:
            self.subjects[subject] = 100

    def average(self):
        """return calc the average of student"""
        if len(self.subjects) == 0:
            return 0
        return sum(self.subjects.values()) / len(self.subjects)

    def __eq__(self, other):
        """equal students by id"""
        if self.id == other.id:
            return True
        else:
            return False

    def __gt__(self, other):
        """greater students by age"""
        if self.age > other.age:
            return True
        else:
            return False

    def __repr__(self):
        return f'|id: {self.id}, name: {self.name}, avg: {self.average()}|'


