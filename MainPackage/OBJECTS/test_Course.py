from unittest import TestCase
from Course import Course
from Student import Student


class TestCourse(TestCase):
    def setUp(self):
        self.c1 = Course(111, "Math", 3)
        self.s_oriel = Student(121, "Oriel", 21)
        self.s_dan = Student(222, "Dan", 30)
        self.s_ben = Student(323, "Ben", 2)

    # check valid arguments in init function
    def test_init_valid(self):
        # check valid id
        self.assertEqual(self.c1.id, 111)
        # check valid name
        self.assertEqual(self.c1.name, "Math")
        # check capacity
        self.assertEqual(self.c1.max, 3)
        self.c1.max = 0
        self.assertEqual(self.c1.max, 0)
        # check students list, and subjects dictionary
        self.assertEqual(self.c1.subjects, {})
        self.assertEqual(self.c1.students, [])
        self.assertTrue(len(self.c1.students) == 0)
        self.assertTrue(len(self.c1.subjects) == 0)

    # check invalid id
    def test_init_invalid_id(self):
        with self.assertRaises(ValueError):
            c1 = Course(0, "Math", 3)
        with self.assertRaises(TypeError):
            c1 = Course("111", "Math", 3)
        with self.assertRaises(TypeError):
            c1 = Course(1.11, "Math", 3)

    # check invalid name
    def test_init_invalid_name(self):
        with self.assertRaises(TypeError):
            c1 = Course(111, 1, 3)
        with self.assertRaises(TypeError):
            c1 = Course(111, ["Math"], 3)

    # check invalid capacity
    def test_init_invalid_max(self):
        with self.assertRaises(TypeError):
            c1 = Course(111, "Math", 0.1)
        with self.assertRaises(ValueError):
            c1 = Course(111, "Math", -1)

    # check valid argument in add_student
    def test_add_student_valid(self):
        # add student
        self.assertTrue(self.c1.add_student(self.s_oriel))
        self.assertIn(self.s_oriel, self.c1.students)
        self.assertTrue(len(self.c1.students) == 1)
        # add more student
        self.assertTrue(self.c1.add_student(self.s_ben))
        self.assertTrue(len(self.c1.students) == 2)
        # add exist student
        self.assertFalse(self.c1.add_student(self.s_ben))
        self.assertTrue(len(self.c1.students) == 2)
        # add 2 student and check if the list full
        s_temp = Student(131, "Kim", 30)
        self.assertTrue(self.c1.add_student(self.s_dan))
        self.assertFalse(self.c1.add_student(s_temp))
        self.assertTrue(len(self.c1.students) == 3)

    # check invalid argument in add_student
    def test_add_student_invalid(self):
        with self.assertRaises(TypeError):
            self.c1.add_student(123)
        with self.assertRaises(TypeError):
            self.c1.add_student(self.s_oriel.name)
        with self.assertRaises(TypeError):
            self.c1.add_student(self.c1)

    def test_del_student_valid(self):
        self.assertTrue(self.c1.add_student(self.s_oriel))

    def test_add_factor(self):
        self.fail()

    # def test_average(self):
    #     self.fail()
    #
    # def test_weak_students(self):
    #     self.fail()
