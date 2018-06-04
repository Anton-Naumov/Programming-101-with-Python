import unittest

from utility import extract_variable_and_power, extract_term


class TestsUnility(unittest.TestCase):
    def test_extract_variable_and_power_raises_exeption(self):
        with self.subTest('With random string'):
            with self.assertRaises(Exception):
                extract_variable_and_power('abc')

        with self.subTest('With no variable: ^2'):
            with self.assertRaises(Exception):
                extract_variable_and_power('^2')

    def tests_extract_variable_and_power(self):
        with self.subTest('No power: x'):
            expected_variable = 'x'
            expected_power = 1

            self.assertEqual(
                (expected_variable, expected_power),
                extract_variable_and_power('x')
            )

        with self.subTest('x^2'):
            expected_variable = 'x'
            expected_power = 2

            self.assertEqual(
                (expected_variable, expected_power),
                extract_variable_and_power('x^2')
            )

    def tests_extract_term_raises_exeption(self):
        with self.subTest('Random string'):
            with self.assertRaises(Exception):
                extract_term('Antonski')

    def tests_extract_term(self):
        with self.subTest('Constant: 2'):
            self.assertEqual(
                (2, 'x', 0),
                extract_term('2')
            )

        with self.subTest('x'):
            self.assertEqual(
                (1, 'x', 1),
                extract_term('x')
            )

        with self.subTest('x^2'):
            self.assertEqual(
                (1, 'x', 2),
                extract_term('x^2')
            )

        with self.subTest('2*x'):
            self.assertEqual(
                (2, 'x', 1),
                extract_term('2*x')
            )

        with self.subTest('2*x^2'):
            self.assertEqual(
                (2, 'x', 2),
                extract_term('2*x^2')
            )


if __name__ == '__main__':
    unittest.main()
