import sys

from polinom import Polinom


def main(function_string):
    f = Polinom.parse_from_string(function_string)
    derived_f = f.derivative()

    print(
        f'Derivative of f(x) = {str(f)} is:\nf\'(x) = {str(derived_f)}'
    )


if __name__ == '__main__':
    main(sys.argv[1])
