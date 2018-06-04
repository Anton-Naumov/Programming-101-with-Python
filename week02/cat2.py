import sys


def cat2(arguments):
    for file_name in arguments:
        with open(file_name) as f:
            print(f.read())


def main():
    cat2(sys.argv[1:])


if __name__ == '__main__':
    main()
