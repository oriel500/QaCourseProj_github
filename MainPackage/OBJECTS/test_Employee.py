from unittest import TestCase
from Employee import Employee


class TestEmployee(TestCase):
    def setUp(self):
        self.emp = Employee("oriel", "naim", 10)

    def test_email(self):
        self.assertEqual("oriel.naim@email.com", self.emp.email())

    def test_fullname(self):
        self.assertEqual("oriel naim", self.emp.fullname())

    def test_apply_raise(self):
        pay1 = self.emp.pay
        amt1 = self.emp.raise_amt
        self.emp.apply_raise()
        self.assertEqual(self.emp.pay, pay1*amt1)
