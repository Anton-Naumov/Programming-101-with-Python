import string
from random import randint, choice


class BookGenerator:
    def __init__(self, chapters_count, chapter_length):
        self.chapters_count = chapters_count
        self.chapter_length = chapter_length

    def generate_word(self):
        word = ''
        for char in range(0, randint(1, 15)):
            word = f'{word}{choice(string.ascii_letters)}'
        if randint(1, 25) == 15:
            word = f'{word}\n'
        word = f'{word} '
        return word

    def generate_chapter(self, number):
        chapter = f'# Chapter {number}\n\n'
        for _ in range(0, self.chapter_length):
            chapter = f'{chapter}{self.generate_word()}'
        chapter = f'{chapter}\n\n'
        return chapter

    def generate_book(self, book_name):
        with open(book_name, 'w') as f:
            for chapter_number in range(0, self.chapters_count):
                f.write(self.generate_chapter(chapter_number))


if __name__ == '__main__':
    book_generator = BookGenerator(100000000000, 200)
    book_generator.generate_book('book1.txt')
