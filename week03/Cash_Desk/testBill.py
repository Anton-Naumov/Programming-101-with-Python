import unittest

from bill import Bill


class TestBill(unittest.TestCase):
    def setUp(self):
        self.a = Bill(10)
        self.b = Bill(5)
        self.c = Bill(10)

    def test___int___method_with_invalid_argument(self):
        with self.assertRaises(TypeError):
            Bill('not integer')
        with self.assertRaises(ValueError):
            Bill(-50)

    def test__init___method_with_valid_amount(self):
        d = Bill(15)
        self.assertEqual(d.amount, 15)

    def test___int__method(self):
        self.assertEqual(int(self.a), int(self.c))
        self.assertNotEqual(int(self.a), int(self.b))

    def test___eq___method(self):
        self.assertEqual(self.a.__eq__(self.b), False)
        self.assertEqual(self.a.__eq__(self.c), True)

    def test___repr___method(self):
        self.assertEqual(repr(self.a), repr(self.c))
        self.assertNotEqual(repr(self.c), repr(self.b))

    def test___hash___method(self):
        test_set = set()
        test_set.add(self.a)
        test_set.add(self.c)
        self.assertEqual(len(test_set), 1)
        test_set.add(self.b)
        self.assertEqual(len(test_set), 2)


if __name__ == '__main__':
    unittest.main()
