import sys


def cat(arguments):
    with open(arguments) as f:
        print(f.read())


def main():
    cat(sys.argv[1])


if __name__ == '__main__':
    main()
