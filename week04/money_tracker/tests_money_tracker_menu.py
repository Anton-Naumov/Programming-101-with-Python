import unittest

from money_tracker_menu import MoneyTrackerMenu


class TestMoneyTrackerMenu(unittest.TestCase):
    def test_date_parser_invalid_dates(self):
        with self.assertRaises(ValueError):
            MoneyTrackerMenu.date_parser('15.12.2018')
        with self.assertRaises(ValueError):
            MoneyTrackerMenu.date_parser('12,12,208')
        with self.assertRaises(ValueError):
            MoneyTrackerMenu.date_parser('abc')
        with self.assertRaises(ValueError):
            MoneyTrackerMenu.date_parser('2018,12,12')

    def test_date_parser_valid_dates(self):
        self.assertEqual(MoneyTrackerMenu.date_parser('12,12,2018'),
                         (12, 12, 2018))
        self.assertEqual(MoneyTrackerMenu.date_parser('5,1,2018'),
                         (5, 1, 2018))

    def test_amount_parser_non_number_argument(self):
        with self.assertRaises(ValueError):
            MoneyTrackerMenu.amount_parser('2018,12,12')
        with self.assertRaises(ValueError):
            MoneyTrackerMenu.amount_parser('abc')

    def test_amount_parser_valid_arguments(self):
        self.assertEqual(MoneyTrackerMenu.amount_parser('123'), 123)
        self.assertEqual(MoneyTrackerMenu.amount_parser('15.5'), 15.5)


if __name__ == '__main__':
    unittest.main()
