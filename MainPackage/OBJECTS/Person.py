from MainPackage.OBJECTS.Student2 import Student


class Person(Student):
    def __init__(self, _age, _num_children, _id, _name, _grade):
        Student.__init__(self, _id, _name, _grade)
        self.age = _age
        self.num_children = _num_children

    def update_grade(self, new_grade):
        if new_grade >= 0:
            self.grade = new_grade

    def has_children(self):
        if self.num_children <= 0:
            return False
        else:
            return True

    def age_group(self):
        if 0 <= self.age <= 18:
            return 'Child'
        elif 19 <= self.age <= 60:
            return 'Adult'
        elif 61 <= self.age <= 120:
            return 'Senior'

    def __str__(self):
        return f'name: {self.name}, age: {self.age}, children: {self.num_children}, grade: {self.grade}'


# == main ==
if __name__ == "__main__":
    name = input("enter name: ")
    age = int(input("enter age: "))
    num_children = int(input("enter number of children: "))

    man = Person(name, age, num_children)
    print(man)
    print(man.has_children())
    print(man.age_group())
