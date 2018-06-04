import sys
from random import randint


def generate_numbers(filename, numbers):
    with open(filename, 'w') as f:
        while numbers > 0:
            f.write(str(randint(1, 1000)) + " ")
            numbers -= 1
        f.write('\n')


def main():
    generate_numbers(sys.argv[1], int(sys.argv[2]))


if __name__ == '__main__':
    main()
