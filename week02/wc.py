import sys


def wc(to_count, file_name):
    with open(file_name) as f:
        content = f.read()
        if to_count == "chars":
            return len(content)
        if to_count == "words":
            return len(content.split(" "))
        if to_count == "lines":
            return len(content.split("\n")) - 1


def main():
    print(wc(sys.argv[1], sys.argv[2]))


if __name__ == '__main__':
    main()
