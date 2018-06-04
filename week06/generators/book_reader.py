from os import listdir
from os.path import isfile, join


class BookReader:
    def __init__(self, path):
        self.sorted_file_names = self.get_sorted_file_names(path)

    def read_chapters(self):
        chapter = []
        for book_file in self.sorted_file_names:
            for line in self.read_file_line(book_file):
                if line.startswith('#'):
                    yield ''.join(chapter)
                    chapter = []
                chapter.append(line)
        yield ''.join(chapter)

    def read_file_line(self, file_name):
        with open(file_name, 'r') as f:
            for line in f:
                yield line

    def read_book(self):
        for chapter in self.read_chapters():
            print(chapter)
            input()

    @staticmethod
    def get_sorted_file_names(path):
        return sorted([join(path, f) for f in listdir(path)
                      if isfile(join(path, f)) and join(path, f).endswith('.txt')])


if __name__ == '__main__':
    book_reader = BookReader('./')
    book_reader.read_book()
