import os
import unittest
from utils import get_datetime_componets, add_one_entry_to_datetime_string
from datetime import datetime
from sql_manager import SQLManager
from exceptions import InvalidPassword, BruteForce


class SqlManagerTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        SQLManager.initialize_database(dbname='test', user='anton')

    def setUp(self):
        SQLManager.drop_clients_table()
        SQLManager.create_clients_table()
        SQLManager.register('Tester', '%thePassword1', 'test@abv.bg')
        self.logged_user = SQLManager.login('Tester', '%thePassword1')

    @classmethod
    def tearDownClass(cls):
        SQLManager.close_database()

    def test_register(self):
        SQLManager.register('Dinko', '#anton1Naumov', 'dinko@abv.bg')

        password = '97bdaf6a2ad8ba5749b5e211288f6972d9ac32aec7ae1b34cf5430c09e313b39'
        SQLManager.cursor.execute('SELECT Count(*)  FROM clients WHERE username = (%s) AND'
                                  ' password = (%s)', ('Dinko', password))

        users_count = SQLManager.cursor.fetchone()

        self.assertEqual(users_count[0], 1)

    def test_login_returns_False_on_wrong_information(self):
        logged_user = SQLManager.login('Tester', 'password')
        self.assertFalse(logged_user)

    def test_login_returns_correct_user(self):
        logged_user = SQLManager.login('Tester', '%thePassword1')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_change_message(self):
        new_message = "podaivinototam"
        SQLManager.change_message(new_message, self.logged_user)
        self.assertEqual(self.logged_user.get_message(), new_message)

    def test_change_password_raises_exception_on_invalid_new_password(self):
        with self.assertRaises(InvalidPassword):
            SQLManager.change_pass('123', self.logged_user)

    def test_change_password(self):
        new_password = "#newPassword123"
        SQLManager.change_pass(new_password, self.logged_user)

        with self.subTest('The password was changed in the database!'):
            password_hash = '9cd9fd430e4be00593e1b2c1824977f1eaee841593a8f44e70bb9261cda5e90d'

            SQLManager.cursor.execute('SELECT Count(*)  FROM clients WHERE username = (%s) AND'
                                      ' password = (%s)', ('Tester', password_hash))

            self.assertEqual(SQLManager.cursor.fetchone()[0], 1)

        with self.subTest('The user can login with the new password!'):
            logged_user_new_password = SQLManager.login('Tester', new_password)
            self.assertEqual(logged_user_new_password.get_username(), 'Tester')


class UtilsTest(unittest.TestCase):
    def test_get_datetime_components_raises_exception_with_invalid_argumet_format(self):
        with self.assertRaisesRegex(Exception, 'Invalid format of argument!'):
            get_datetime_componets('abc')

    def test_get_datetime_components_with_datetime_string_with_two_parts(self):
        part1, part2, part3 = get_datetime_componets('2018-05-24 22:00:59#5')

        self.assertEqual(part1, datetime(2018, 5, 24, hour=22, minute=0, second=59))
        self.assertEqual(part2, 5)
        self.assertEqual(part3, None)

    def test_get_datetime_components_with_datetime_string_with_three_parts(self):
        part1, part2, part3 = get_datetime_componets('2018-05-24 22:00:59#5'
                                                     '#2018-05-24 22:00:59')
        dt = datetime(2018, 5, 24, hour=22, minute=0, second=59)

        self.assertEqual(part1, dt)
        self.assertEqual(part2, 5)
        self.assertEqual(part3, dt)

    def test_add_one_entry_to_datetime_string(self):
        with self.subTest('When more than the penalty time has passed sinse last faliled try!'):
            expected = '2018-05-24 22:06:59#1'

            dt = datetime(2018, 5, 24, hour=22, minute=6, second=59)
            result = add_one_entry_to_datetime_string('2018-05-24 22:00:59#4', dt)

            self.assertEqual(expected, result)

        with self.subTest('Exception is raised during the penalty time'):
            dt = datetime(2018, 5, 24, hour=22, minute=8, second=00)

            with self.assertRaisesRegex(BruteForce, 'There are 3 minutes penalty!'):
                add_one_entry_to_datetime_string('2018-05-24 22:00:59#5#'
                                                 '2018-05-24 22:05:00', dt)

        with self.subTest('When the current entry tringgers the penalty'):
            expected = '2018-05-24 22:08:00#10#2018-05-24 22:08:00'

            dt = datetime(2018, 5, 24, hour=22, minute=8, second=00)
            result = add_one_entry_to_datetime_string('2018-05-24 22:05:59#9', dt)

            self.assertEqual(expected, result)

        with self.subTest('The first entry after the penalty, removes the last part of the msg'):
            expected = '2018-05-24 22:16:00#11'

            dt = datetime(2018, 5, 24, hour=22, minute=16, second=00)
            result = add_one_entry_to_datetime_string('2018-05-24 22:05:59#10'
                                                      '#2018-05-24 22:05:59', dt)

            self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
