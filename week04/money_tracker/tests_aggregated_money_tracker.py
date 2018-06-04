import unittest

from aggregated_money_tracker import AgregatedMoneyTracker
from category import Expense, Income


class TestsAgregatedMoneyTracker(unittest.TestCase):
    def setUp(self):
        self.agr_money_tracker = AgregatedMoneyTracker()
        self.agr_money_tracker._data = {'2018,11,12': {
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

    def test_get_sorted_dates(self):
        self.assertEqual(self.agr_money_tracker.get_sorted_dates(),
                         ['2018,11,12', '2018,11,15', '2018,11,17'])

    def test_get_date_str_invalid_data(self):
        with self.assertRaises(ValueError):
            AgregatedMoneyTracker.get_date_str('11,12,2018')

    def test_get_date_str_valid_data(self):
        self.assertEqual(AgregatedMoneyTracker.get_date_str('2018,11,12'),
                         '=== 12-11-2018 ===\n')

    def test_str_empty_data(self):
        self.assertEqual(str(AgregatedMoneyTracker()), '')

    def test_str_(self):
        expected_result = ('=== 12-11-2018 ===\n'
                           '5, food, New Expense\n'
                           '=== 15-11-2018 ===\n'
                           '50, salary, New Income\n'
                           '100, shoes, New Expense\n'
                           '=== 17-11-2018 ===\n'
                           '20, clothes, New Income\n')
        self.assertEqual(str(self.agr_money_tracker), expected_result)

    def test_set_record_date_wrong_date_format(self):
        with self.assertRaises(ValueError):
            self.agr_money_tracker.set_record_for_date('12,12,2018',
                                                       '5, water,'
                                                       'New Expense\n')

    def test_set_record_for_date_with_old_date(self):
        expected_result = {'2018,11,12': {
                                          'income': [],
                                          'expence': [Expense('food', 5)]
                                         },
                           '2018,11,15': {
                                          'income': [Income('salary', 50)],
                                          'expence': [Expense('shoes', 100)]
                                         },
                           '2018,11,17': {
                                           'income': [Income('clothes', 20)],
                                           'expence': [Expense('water', 5)]
                                         }}
        self.agr_money_tracker.set_record_for_date('2018,11,17',
                                                   '5, water, New Expense\n')
        self.assertEqual(self.agr_money_tracker._data, expected_result)

    def test_set_record_for_date_with_new_date(self):
        expected_result = {'2018,11,12': {
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
                                         },
                           '2018,12,12': {
                                            'income': [],
                                            'expence': [Expense('water', 5)]
                                         }}
        self.agr_money_tracker.set_record_for_date('2018,12,12',
                                                   '5, water, New Expense\n')
        self.assertEqual(self.agr_money_tracker._data, expected_result)

    def test_set_record_for_date_with_Expense_or_Income_new_record(self):
        expected_result = {'2018,11,12': {
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
                                         },
                           '2018,12,12': {
                                            'income': [],
                                            'expence': [Expense('water', 5)]
                                         }}
        self.agr_money_tracker.set_record_for_date('2018,12,12',
                                                   Expense('water', 5))
        self.assertEqual(self.agr_money_tracker._data, expected_result)

    def test_get_expences_for_date_date_with_no_records(self):
        self.assertEqual(self.agr_money_tracker.get_expences_for_date('2018,'
                                                                      '1,1'),
                         [])

    def test_get_expences_for_date_date_with_records(self):
        self.assertEqual(self.agr_money_tracker.get_expences_for_date('2018,'
                                                                      '11,15'),
                         [Expense('shoes', 100)])

    def test_get_income_for_date_date_with_no_records(self):
        self.assertEqual(self.agr_money_tracker.get_income_for_date('2018,'
                                                                    '1,1'),
                         [])

    def test_get_income_for_date_date_with_records(self):
        self.assertEqual(self.agr_money_tracker.get_income_for_date('2018,'
                                                                    '11,15'),
                         [Income('salary', 50)])


if __name__ == '__main__':
    unittest.main()
