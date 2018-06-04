import unittest

from term import Term


class TestsTerm(unittest.TestCase):
    def test__init__validations(self):
        with self.subTest('Negative coeff'):
            with self.assertRaises(AttributeError):
                Term(coeff=-2, variable='x', power=2)

        with self.subTest('Negative power'):
            with self.assertRaises(AttributeError):
                Term(coeff=2, variable='x', power=-2)

        with self.subTest('Invalid variable'):
            with self.assertRaises(AttributeError):
                Term(coeff=2, variable='var', power=2)

        with self.subTest('Valid arguments'):
            Term(coeff=5, variable='x', power=55)

    def test__init__default_parameters(self):
        expected = Term(coeff=2, power=2)
        self.assertEqual(expected, Term(coeff=2, variable='x', power=2))

    def test_constant(self):
        expected = Term.constant(5)
        self.assertEqual(expected, Term(coeff=5, variable='x', power=0))

    def tests__str__working_correctly(self):
        with self.subTest('Coeff = 0: 0'):
            term = Term(coeff=0, power=2)
            self.assertEqual(str(term), '0')

        with self.subTest('Power = 0: 2'):
            term = Term.constant(2)
            self.assertEqual(str(term), '2')

        with self.subTest('Coeff = 1: x^2'):
            term = Term(coeff=1, power=2)
            self.assertEqual(str(term), 'x^2')

        with self.subTest('Power = 1: 2*x'):
            term = Term(coeff=2, power=1)
            self.assertEqual(str(term), '2*x')

        with self.subTest('Coeff = 1 and Power = 1: x'):
            term = Term(coeff=1, power=1)
            self.assertEqual(str(term), 'x')

        with self.subTest('All positive arguments: 2*x^2'):
            term = Term(coeff=2, power=2)
            self.assertEqual(str(term), '2*x^2')

    def test_is_property(self):
        with self.subTest('True'):
            term = Term.constant(7)
            self.assertTrue(term.is_constant)

        with self.subTest('False'):
            term = Term(coeff=5, power=1)
            self.assertFalse(term.is_constant)

    def tests__eq__not_equal(self):
        with self.subTest('Only coeff differ'):
            term1 = Term(coeff=1, power=2)
            term2 = Term(coeff=2, power=2)
            self.assertFalse(term1 == term2)

        with self.subTest('Only variable differ'):
            term1 = Term(coeff=1, variable='x', power=2)
            term2 = Term(coeff=1, variable='y', power=2)
            self.assertFalse(term1 == term2)

        with self.subTest('Only power differ'):
            term1 = Term(coeff=2, power=1)
            term2 = Term(coeff=2, power=2)
            self.assertFalse(term1 == term2)

        with self.subTest('Only coeffs are equal'):
            term1 = Term(coeff=1, variable='x', power=2)
            term2 = Term(coeff=1, variable='y', power=3)
            self.assertFalse(term1 == term2)

        with self.subTest('Only variables are equal'):
            term1 = Term(coeff=1, power=1)
            term2 = Term(coeff=2, power=2)
            self.assertFalse(term1 == term2)

        with self.subTest('Only powers are eqal'):
            term1 = Term(coeff=1, variable='x', power=2)
            term2 = Term(coeff=2, variable='y', power=2)
            self.assertFalse(term1 == term2)

    def test__eq__are_equal(self):
        term1 = Term(coeff=1, power=5)
        term2 = Term(coeff=1, power=5)
        self.assertTrue(term1 == term2)

    def test_parse_term_with_invalid_string(self):
        with self.assertRaises(Exception):
            Term.parse_term('2*2*x')

    def test_parse_term_with_valid_strings(self):
        with self.subTest('2'):
            term = Term.parse_term('2')
            expected_term = Term.constant(2)

            self.assertEqual(term, expected_term)

        with self.subTest('x'):
            term = Term.parse_term('x')
            expected_term = Term(coeff=1, variable='x', power=1)

            self.assertEqual(term, expected_term)

        with self.subTest('x^2'):
            term = Term.parse_term('x^2')
            expected_term = Term(coeff=1, variable='x', power=2)

            self.assertEqual(term, expected_term)

        with self.subTest('2*x'):
            term = Term.parse_term('2*x')
            expected_term = Term(coeff=2, variable='x', power=1)

            self.assertEqual(term, expected_term)

        with self.subTest('2*x^2'):
            term = Term.parse_term('2*x^2')
            expected_term = Term(coeff=2, variable='x', power=2)

            self.assertEqual(term, expected_term)

    def test__add__raises_exception(self):
        with self.subTest('Terms with different variables'):
            term1 = Term(coeff=1, variable='x', power=2)
            term2 = Term(coeff=1, variable='y', power=2)

            with self.assertRaises(AssertionError):
                term1 + term2

        with self.subTest('Terms with different powers'):
            term1 = Term.constant(1)
            term2 = Term(coeff=1, power=2)

            with self.assertRaises(AssertionError):
                term1 + term2

        with self.subTest('Terms with different variables and powers'):
            term1 = Term(coeff=1, variable='x', power=2)
            term2 = Term(coeff=1, variable='y', power=3)

            with self.assertRaises(AssertionError):
                term1 + term2

    def test__add__(self):
        term1 = Term(coeff=5, power=2)
        term2 = Term(coeff=2, power=2)
        result = term1 + term2
        expected_result = Term(coeff=7, power=2)

        self.assertEqual(expected_result, result)

    def test_derivative(self):
        with self.subTest('constant'):
            term = Term.constant(5)
            expected = Term.constant(0)

            self.assertEqual(expected, term.derived)

    def test__gt__(self):
        term1 = Term(coeff=5, power=1)
        term2 = Term(coeff=2, power=2)

        self.assertTrue(term2 > term1)
        self.assertFalse(term1 > term2)


if __name__ == '__main__':
    unittest.main()
