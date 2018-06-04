import unittest

from client import Client
from exceptions import InvalidPassword


class ClientTests(unittest.TestCase):

    def setUp(self):
        self.test_client = Client(1, "Ivo", 200000.00,
                                  'Bitcoin mining makes me rich', "ivo@abv.bg")

    def test_client_id(self):
        self.assertEqual(self.test_client.get_id(), 1)

    def test_client_name(self):
        self.assertEqual(self.test_client.get_username(), "Ivo")

    def test_client_balance(self):
        self.assertEqual(self.test_client.get_balance(), 200000.00)

    def test_client_message(self):
        self.assertEqual(self.test_client.get_message(), "Bitcoin mining makes me rich")

    def test_validate_password_returns_False(self):
        with self.subTest('username is substring of the password!'):
            with self.assertRaisesRegex(InvalidPassword,
                                        'The password should\'t contain the username!'):
                Client.validate_password('#Antonski1', 'tons')

        with self.subTest('password is shorter than 8 symbols'):
            with self.assertRaisesRegex(InvalidPassword,
                                        'The password should be longer then 8 symbols!'):
                Client.validate_password('#Aa1arg', 'Z')

        with self.subTest('passwort does\'t contain any digits'):
            with self.assertRaisesRegex(InvalidPassword,
                                        'The password must contain a digit!'):
                Client.validate_password('#Aaargqwe', 'Z')

        with self.subTest('passwort does\'t contain any capital letters'):
            with self.assertRaisesRegex(InvalidPassword,
                                        'The password must contain a capital letter!'):
                Client.validate_password('#aargqwe1', 'Z')

        with self.subTest('passwort does\'t contain any special symbol'):
            with self.assertRaisesRegex(InvalidPassword,
                                        'The password must contain a special symbol!'):
                Client.validate_password('Aaargqwe1', 'Z')

    def test_validate_password_returns_True(self):
        try:
            Client.validate_password('#anton1Naumov', 'Toni')
        except InvalidPassword as e:
            self.fail(e)


if __name__ == '__main__':
    unittest.main()
