import unittest

from functions_tests01 import (sum_of_digits, to_digits, to_number,
                               fact_digits, fibonacci, nth_fibonacci)


class Functions_tests01(unittest.TestCase):
    def test_task01_input(self):
        with self.assertRaises(AssertionError):
            sum_of_digits("str")
            sum_of_digits([1, 2, 3])

    def test_task01_negative_number(self):
        self.assertEqual(sum_of_digits(-10), 1)

    def test_task01_positive_number(self):
        self.assertEqual(sum_of_digits(1325132435356), 43)
        self.assertEqual(sum_of_digits(123), 6)
        self.assertEqual(sum_of_digits(6), 6)

    def test_to_digits_input(self):
        with self.assertRaises(AssertionError):
            to_digits("str")
        with self.assertRaises(AssertionError):
            to_digits({1: 'a', 2: 'b'})

    def test_to_digits_random_positive_numbers(self):
        self.assertEqual(to_digits(123), [1, 2, 3])
        self.assertEqual(to_digits(99999), [9, 9, 9, 9, 9])
        self.assertEqual(to_digits(123023), [1, 2, 3, 0, 2, 3])

    def test_to_digits_negative_number(self):
        self.assertEqual(to_digits(-123), [1, 2, 3])

    def test_to_number_input(self):
        with self.assertRaises(AssertionError):
            to_number("str")
            to_number(12345)
            to_number({})

    def test_to_number_empty_list(self):
        self.assertEqual(to_number([]), 0)

    def test_to_number_normal_tests(self):
        self.assertEqual(to_number([1, 2, 3]), 123)
        self.assertEqual(to_number([9, 9, 9, 9, 9]), 99999)
        self.assertEqual(to_number([1, 2, 3, 0, 2, 3]), 123023)
        self.assertEqual(to_number([21, 2, 33]), 21233)

    def test_fact_digits_input(self):
        with self.assertRaises(AssertionError):
            fact_digits("str")
            fact_digits([1, 2, 3, 4, 5])
            fact_digits(set())

    def test_fact_digits_result_tests(self):
        self.assertEqual(fact_digits(111), 3)
        self.assertEqual(fact_digits(145), 145)
        self.assertEqual(fact_digits(999), 1088640)

    def test_nth_fibonacci_invalid_input(self):
        with self.assertRaises(AssertionError):
            nth_fibonacci("str")
            nth_fibonacci([])

    def test_nth_fibonacci_negative_argument(self):
        self.assertEqual(nth_fibonacci(-10), 55)

    def test_nth_fibonacci_random_input(self):
        self.assertEqual(nth_fibonacci(8), 21)
        self.assertEqual(nth_fibonacci(12), 144)
        self.assertEqual(nth_fibonacci(3), 2)
        self.assertEqual(nth_fibonacci(2), 1)

    def test_fibonacci_input_tests(self):
        with self.assertRaises(AssertionError):
            fibonacci("str")
            fibonacci([])

    def test_fibonacci_negative_input(self):
        self.assertEqual(fibonacci(-4), [1, 1, 2, 3])

    def test_fibonacci_random_input(self):
        self.assertEqual(fibonacci(1), [1])
        self.assertEqual(fibonacci(2), [1, 1])
        self.assertEqual(fibonacci(3), [1, 1, 2])
        self.assertEqual(fibonacci(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])


if __name__ == '__main__':
    unittest.main()
