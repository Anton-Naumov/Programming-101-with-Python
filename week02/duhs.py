import sys
import os

# za zadachata da se polzva - grouping by


def size(directory_path):
    total_size = 0
    for root, dirs, files in os.walk(directory_path):
        for direction in dirs:
            total_size += size(os.path.join(root, direction))
        for file in files:
            total_size += os.path.getsize(os.path.join(root, file))
    return total_size // 1024 // 1024


def main():
    print("The directory \"{0}\" size is {1} MB:".format(sys.argv[1],
          size(sys.argv[1])))


if __name__ == '__main__':
    main()
