import unittest

from category import Expense, Income


class TestCategoryExpenseIncome(unittest.TestCase):
    def setUp(self):
        self.expence = Expense('food', 5)
        self.income = Income('salary', 10.55)

    def test_str_expence(self):
        self.assertEqual(str(self.expence), '5, food, New Expense\n')

    def test_eq_expence(self):
        self.assertNotEqual(self.expence, Expense('clotes', 5))
        self.assertNotEqual(self.expence, Expense('food', 10))
        self.assertEqual(self.expence, Expense('food', 5))

    def test_str_income(self):
        self.assertEqual(str(self.income), '10.55, salary, New Income\n')

    def test_eq_income(self):
        self.assertNotEqual(self.income, Income('salary', 5))
        self.assertNotEqual(self.income, Income('food', 10.55))
        self.assertEqual(self.income, Income('salary', 10.55))


if __name__ == '__main__':
    unittest.main()
