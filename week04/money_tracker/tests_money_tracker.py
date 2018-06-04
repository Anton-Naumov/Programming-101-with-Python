import unittest

from money_tracker import MoneyTracker
from aggregated_money_tracker import AgregatedMoneyTracker
from category import Expense, Income


class TestsMoneyTracker(unittest.TestCase):
    def setUp(self):
        agr_money_tracker = AgregatedMoneyTracker()
        agr_money_tracker._data = {'2018,11,12': {
                                          'income': [],
                                          'expence': [Expense('food', 5)]
                                    },
                                   '2018,11,15': {
                                          'income': [Income('salary', 50)],
                                          'expence': [Expense('shoes', 100)]
                                    },
                                   '2018,11,17': {
                                          'income': [Income('clothes', 20)],
                                          'expence': []
                                   }}
        self.money_tracker = MoneyTracker()
        self.money_tracker._data_base = agr_money_tracker

    def test_list_user_data(self):
        expected_result = ('=== 12-11-2018 ===\n'
                           '5, food, New Expense\n'
                           '=== 15-11-2018 ===\n'
                           '50, salary, New Income\n'
                           '100, shoes, New Expense\n'
                           '=== 17-11-2018 ===\n'
                           '20, clothes, New Income\n')
        self.assertEqual(self.money_tracker.list_user_data(), expected_result)

    def test_get_string_with_empty_data(self):
        self.assertEqual(MoneyTracker.get_string([]), '')

    def test_get_string_with_data(self):
        self.assertEqual(MoneyTracker.get_string([1, 2, 3]), '123')
        self.assertEqual(MoneyTracker.get_string([Income('salary', 50),
                                                  Expense('shoes', 100)]),
                         ('50, salary, New Income\n'
                          '100, shoes, New Expense\n'))

    def test_show_user_data_per_date_no_data_for_the_date(self):
        self.assertEqual(self.money_tracker.show_user_data_per_date(5, 5,
                                                                    2010),
                         '')

    def test_show_user_data_per_date(self):
        self.assertEqual(self.money_tracker.show_user_data_per_date(15, 11,
                                                                    2018),
                         '50, salary, New Income\n'
                         '100, shoes, New Expense\n')

    def test_get_user_income_no_income(self):
        self.assertEqual(MoneyTracker().get_user_incomes(), [])

    def test_get_user_income(self):
        self.assertEqual(self.money_tracker.get_user_incomes(),
                         [Income('salary', 50), Income('clothes', 20)])

    def test_get_user_expences_no_income(self):
        self.assertEqual(MoneyTracker().get_user_expences(), [])

    def test_get_user_expences(self):
        self.assertEqual(self.money_tracker.get_user_expences(),
                         [Expense('food', 5), Expense('shoes', 100)])

    def test_show_user_income(self):
        self.assertEqual(self.money_tracker.show_user_incomes(),
                         '50, salary, New Income\n'
                         '20, clothes, New Income\n')

    def test_show_user_expences(self):
        self.assertEqual(self.money_tracker.show_user_expences(),
                         '5, food, New Expense\n'
                         '100, shoes, New Expense\n')

    def test_list_income_categories_with_no_categories(self):
        self.assertEqual(MoneyTracker().list_income_categories(), '')

    def test_list_income_categories(self):
        self.assertEqual(self.money_tracker.list_income_categories(),
                         'salary\n'
                         'clothes\n')

    def test_list_expence_categories_with_no_categories(self):
        self.assertEqual(MoneyTracker().list_expence_categories(), '')

    def test_list_expece_categories(self):
        self.assertEqual(self.money_tracker.list_expence_categories(),
                         'food\n'
                         'shoes\n')

    def test_list_user_exepences_ordered_by_categories(self):
        self.money_tracker._data_base.set_record_for_date('2018,11,17',
                                                          '10, book, '
                                                          'New Expense\n')
        exp = self.money_tracker.list_user_exepences_ordered_by_categories()
        self.assertEqual(exp, '10, book, New Expense\n'
                              '5, food, New Expense\n'
                              '100, shoes, New Expense\n')


if __name__ == '__main__':
    unittest.main()
