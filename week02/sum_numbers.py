import sys


def sum_numbers(filename):
    result = 0
    with open(filename, 'r') as f:
        numbers_line = f.readline().split(" ")
        for number_str in numbers_line[:-1]:
            result += int(number_str)
    print(result)


def main():
    sum_numbers(sys.argv[1])


if __name__ == '__main__':
    main()
