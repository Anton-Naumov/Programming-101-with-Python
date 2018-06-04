import unittest

from utility import format_length


class TestUtility(unittest.TestCase):
    def test_format_length(self):
        with self.subTest('With minutes and seconds less than 60'):
            self.assertEqual(
                format_length(1, 25, 54),
                (1, 25, 54)
            )

        with self.subTest('With seconds more than 60'):
            self.assertEqual(
                format_length(1, 25, 65),
                (1, 26, 5)
            )

        with self.subTest('With minutes more than 60'):
            self.assertEqual(
                format_length(1, 75, 55),
                (2, 15, 55)
            )

        with self.subTest('With minutes and seconds more than 60'):
            self.assertEqual(
                format_length(1, 64, 65),
                (2, 5, 5)
            )


if __name__ == '__main__':
    unittest.main()
