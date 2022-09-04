# main file of objects: Student and Course
from Student import Student
from Course import Course

print("===CREATE COURSE===")
id_course = int(input("Please enter id for new course: "))
name_course = input("Please enter name of course: ")
max_num_students = int(input("Please enter max number of student to take in: "))
course = Course(id_course, name_course, max_num_students)
print("======================================================================")

print("===ADD SUBJECTS===")
print("# add the number 0 to end the input #")
new_subject = ""
while True:
    new_subject = input("Enter subject: ")
    if new_subject == "0":
        break
    teacher = input(f"Enter name for the teacher to subject {new_subject.capitalize()}: ")
    course.subjects[new_subject] = teacher
print(course)
print("======================================================================")

print("===ADD STUDENTS TO COURSE===")
print("# write id 0 to end the input #")
id_student = int(input(f"Enter id of the student: "))

while id_student != 0:
    if id_student == 0:
        break
    name_student = input("Enter name: ")
    age_student = int(input("Enter age: "))
    new_student = Student(id_student, name_student, age_student)
    # add grade to all subjects
    for subject in course.subjects:
        grade = float(input(f"Enter grade to subject {subject}: "))
        new_student.add_grade(subject, grade)
    # add student to course
    is_add = course.add_student(new_student)
    if not is_add:
        break
    id_student = int(input(f"Enter id of the student: "))
print(course)
print("======================================================================")
# add factor to course
subject_factor = input("\nType subject to add factor: ")
factor1 = int(input("Enter factor: "))
course.add_factor(subject_factor, factor1)
print(course)

print("======================================================================")
# remove the weak students
tuple_index_min_avg_grade = course.weak_students()
if len(course.students) > 0:
    for i in tuple_index_min_avg_grade:
        delete_student = course.students[i]
        course.del_student(delete_student)
print("\n", course)

print("======================================================================")
print("\n", max(course.students))

