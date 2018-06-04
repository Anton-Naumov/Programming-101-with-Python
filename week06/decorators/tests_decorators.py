import unittest

from decorators import accepts


@accepts(str, int)
def acceptTestFunc(string, integer):
    return f'{string} {integer}'


class TestDecorators(unittest.TestCase):
    def test_accept_raises_exception_when_args_types_do_not_match_the_decorator_args(self):
        with self.subTest('Second arg type does not match the decorator arg'):
            with self.assertRaises(TypeError) as e:
                acceptTestFunc('str', 'str')

            self.assertEqual(
                str(e.exception),
                'Argument 1 of acceptTestFunc is not int'
            )

        with self.subTest('Both arg types do not match the decorator args'):
            with self.assertRaises(TypeError) as e:
                acceptTestFunc([], [])

            self.assertEqual(
                str(e.exception),
                'Argument 0 of acceptTestFunc is not str'
            )

    def test_accept_decorator_doesnt_change_the_func_output(self):
        with self.subTest('Func args types match the decorators args'):
            self.assertEqual(
                acceptTestFunc('Anton', 20),
                'Anton 20'
            )


if __name__ == '__main__':
    unittest.main()
