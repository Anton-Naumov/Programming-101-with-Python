import unittest

from parse_money_tracker_data import ParseMoneyTrackerData as ParseMTD
from category import Income, Expense


class TestCategoryExpenseIncome(unittest.TestCase):
    def setUp(self):
        self.dates_dict = {'2018,11,12': {
                                            'income': [Income('salary', 50)],
                                            'expence': [Expense('food', 5)]
                                         },
                           '2018,11,15': {
                                            'income': [],
                                            'expence': [Expense('shoes', 100)]
                                         },
                           '2018,11,17': {
                                           'income': [],
                                           'expence': [Expense('clothes', 20)]
                                         }}

    def test_parse_date_argument_not_matching_the_date_re(self):
        self.assertEqual(ParseMTD.parse_date('12,05,2018'), None)

    def test_parse_date_argument_matching_the_date_re(self):
        self.assertEqual(ParseMTD.parse_date('=== 12-5-2018 ===\n'),
                         '2018,5,12')

    def test_parse_expence_argument_not_matching_the_exepence_re(self):
        self.assertEqual(ParseMTD.parse_expence('food, 5.50, New Expense\n'),
                         None)

    def test_parse_expence_argument_matching_the_exepence_re(self):
        self.assertEqual(ParseMTD.parse_expence('5, food, New Expense\n'),
                         Expense('food', 5))
        self.assertEqual(ParseMTD.parse_expence('5.50, food, New Expense\n'),
                         Expense('food', 5.50))

    def test_parse_income_argument_not_matching_the_income_re(self):
        self.assertEqual(ParseMTD.parse_income('salary, 2500, New Income\n'),
                         None)

    def test_parse_income_argument_matching_the_income_re(self):
        self.assertEqual(ParseMTD.parse_income('2500, salary, New Income\n'),
                         Income('salary', 2500))
        self.assertEqual(ParseMTD.parse_income('15.50, food, New Income\n'),
                         Income('food', 15.50))

    def tests_parse_row_argument_matching_the_date_re(self):
        self.assertEqual(ParseMTD.parse_row('=== 12-11-2018 ===\n'),
                         '2018,11,12')

    def tests_parse_row_argument_matching_the_expence_re(self):
        self.assertEqual(ParseMTD.parse_row('5.5, Eating out, New Expense\n'),
                         Expense('Eating out', 5.5))

    def tests_parse_row_argument_matching_the_income_re(self):
        self.assertEqual(ParseMTD.parse_row('25, luck, New Income\n'),
                         Income('luck', 25))

    def tests_parse_row_argument_not_matching_any_re(self):
        with self.assertRaises(ValueError):
            ParseMTD.parse_row('Antonski')

    def test_add_record_raw_record_containig_date(self):
        self.assertEqual(ParseMTD.add_record(self.dates_dict, '',
                                             '2018,11,12'),
                         (self.dates_dict, '2018,11,12'))

    def test_add_record_with_date_in_the_dates_dict(self):
        dates_dict_result = {'2018,11,12': {
                                            'income': [Income('salary', 50)],
                                            'expence': [Expense('food', 5),
                                                        Expense('computer',
                                                                2500)]
                                         },
                             '2018,11,15': {
                                            'income': [],
                                            'expence': [Expense('shoes', 100)]
                                         },
                             '2018,11,17': {
                                           'income': [],
                                           'expence': [Expense('clothes', 20)]
                                         }}
        self.assertEqual(ParseMTD.add_record(self.dates_dict, '2018,11,12',
                                             Expense('computer', 2500)),
                         (dates_dict_result, '2018,11,12'))

    def test_add_record_with_date_not_in_dates_dict(self):
        dates_dict_result = {'2018,11,12': {
                                            'income': [Income('salary', 50)],
                                            'expence': [Expense('food', 5)]
                                         },
                             '2018,11,15': {
                                            'income': [],
                                            'expence': [Expense('shoes', 100)]
                                         },
                             '2018,11,17': {
                                           'income': [],
                                           'expence': [Expense('clothes', 20)]
                                         },
                             '2018,5,11': {
                                            'income': [Income('paycheck', 10)],
                                            'expence': []
                                          }}
        self.assertEqual(ParseMTD.add_record(self.dates_dict, '2018,5,11',
                                             Income('paycheck', 10)),
                         (dates_dict_result, '2018,5,11'))

    def test_parse_lines_with_no_lines(self):
        self.assertEqual(ParseMTD.parse_lines([]), {})

    def test_parse_lines_with_lines(self):
        info = ['=== 12-11-2018 ===\n',
                '5, food, New Expense\n',
                '50, salary, New Income\n',
                '=== 15-11-2018 ===\n',
                '100, shoes, New Expense\n',
                '=== 17-11-2018 ===\n',
                '20, clothes, New Expense\n']
        self.assertEqual(ParseMTD.parse_lines(info), self.dates_dict)


if __name__ == '__main__':
    unittest.main()
