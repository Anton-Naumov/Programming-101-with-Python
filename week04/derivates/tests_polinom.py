import unittest

from term import Term
from polinom import Polinom


class TestPolinom(unittest.TestCase):
    def setUp(self):
        self.term1 = Term.constant(5)
        self.term2 = Term(coeff=2, power=2)
        self.term3 = Term(coeff=5, power=3)
        self.p = Polinom([self.term1, self.term2, self.term3])

    def test__init__(self):
        with self.subTest('Empty terms'):
            p = Polinom([])

            self.assertEqual(p._terms, {})

        with self.subTest('With terms'):
            expected_dict = {
                0: self.term1,
                2: self.term2,
                3: self.term3
            }

            self.assertEqual(self.p._terms, expected_dict)

    def tests_add_term_with_power_not_already_in_the_terms(self):
        with self.subTest('Term power not already in the terms'):
            term = Term(coeff=3, power=4)

            expected = {
                0: self.term1,
                2: self.term2,
                3: self.term3,
                4: term
            }
            self.p.add_term(term)

            self.assertEqual(expected, self.p._terms)

    def tests_add_term_with_power_already_in_the_terms(self):
        with self.subTest('Term power already in the terms'):
            term = Term.constant(4)

            expected = {
                0: self.term1 + term,
                2: self.term2,
                3: self.term3,
            }
            self.p.add_term(term)

            self.assertEqual(expected, self.p._terms)

    def test__str__(self):
        with self.subTest('Prints all terms sorted'):
            self.p.add_term(Term.constant(0))
            expected = '5*x^3 + 2*x^2 + 5'

            self.assertEqual(expected, str(self.p))

        with self.subTest('With a term that is: 0'):
            self.p.add_term(Term.constant(0))
            expected = '5*x^3 + 2*x^2 + 5'

            self.assertEqual(expected, str(self.p))

    def test_derivative(self):
        derivative = self.p.derivative()

        expected = {
            0: self.term1.derived,
            1: self.term2.derived,
            2: self.term3.derived
        }

        self.assertEqual(expected, derivative._terms)

    def test_parse_from_string(self):
        expected = {
            0: self.term1,
            2: self.term2,
            3: self.term3,
        }

        polinom = Polinom.parse_from_string('5+2*x^2+5*x^3')

        self.assertEqual(expected, polinom._terms)


if __name__ == '__main__':
    unittest.main()
