import unittest

from testing import (validate_fraction, simplify_fraction,
                     collect_fractions, sort_fractions)


class Testing_testing02(unittest.TestCase):
    def test_validate_fraction_not_tuple(self):
        with self.assertRaises(ValueError):
            validate_fraction("str")
        with self.assertRaises(ValueError):
            validate_fraction(123)

    def test_validate_fraction_zero_denom(self):
        with self.assertRaises(ZeroDivisionError):
            validate_fraction((1, 0))

    def test_simplify_fraction_input_not_typle(self):
        with self.assertRaises(ValueError):
            simplify_fraction("str")
        with self.assertRaises(ValueError):
            simplify_fraction(123)
        with self.assertRaises(ValueError):
            simplify_fraction([])

    def test_simplify_fraction_input_invalid_tuple(self):
        with self.assertRaises(ValueError):
            simplify_fraction((1, 2, 3))
        with self.assertRaises(ValueError):
            simplify_fraction(('a', []))

    def test_simplify_fraction_with_denominator_zero(self):
        with self.assertRaises(ZeroDivisionError):
            simplify_fraction((1, 0))

    def test_simplify_fraction_random_tests(self):
        self.assertEqual(simplify_fraction((3, 9)), (1, 3))
        self.assertEqual(simplify_fraction((1, 7)), (1, 7))
        self.assertEqual(simplify_fraction((4, 10)), (2, 5))
        self.assertEqual(simplify_fraction((63, 462)), (3, 22))
        self.assertEqual(simplify_fraction((101, 1001)), (101, 1001))
        self.assertEqual(simplify_fraction((6, 8)), (3, 4))

    def test_colect_fractions_validation(self):
        with self.assertRaises(ValueError):
            collect_fractions("str")
        with self.assertRaises(ValueError):
            collect_fractions({})
        with self.assertRaises(ValueError):
            collect_fractions([(1, 2), (4, 5), ('a', 'b')])
        with self.assertRaises(ZeroDivisionError):
            collect_fractions([(1, 1), (2, 0)])

    def test_collect_fractions_random_fractions(self):
        self.assertEqual(collect_fractions([(1, 4), (1, 2)]), (3, 4))
        self.assertEqual(collect_fractions([(1, 7), (2, 6)]), (10, 21))
        self.assertEqual(collect_fractions([(1, 1), (1, 2), (1, 3)]), (11, 6))

    def test_sort_fractions_input_not_list(self):
        with self.assertRaises(ValueError):
            sort_fractions("str")
        with self.assertRaises(ValueError):
            sort_fractions(123)

    def test_sort_fractions_input_invalid_list(self):
        with self.assertRaises(ValueError):
            sort_fractions([(1, 2), "123"])
        with self.assertRaises(ValueError):
            sort_fractions([(1, 2), ('a', 'b')])

    def test_sort_fractions_with_valid_input(self):
        self.assertEqual(sort_fractions([]), [])
        self.assertEqual(sort_fractions([(2, 3), (1, 2)]), [(1, 2), (2, 3)])
        self.assertEqual(sort_fractions([(2, 3), (1, 2), (1, 3)]),
                         [(1, 3), (1, 2), (2, 3)])
        self.assertEqual(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8),
                                         (9, 6), (15, 32)]),
                         [(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)])


if __name__ == '__main__':
    unittest.main()
