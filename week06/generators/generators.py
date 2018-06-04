def chain(iterable_one, idterable_two):
    yield from iterable_one
    yield from idterable_two


def compress(iterable, mask):
    for item, to_return in zip(iterable, mask):
        if to_return:
            yield item


def cycle(iterable):
    while True:
        for item in iterable:
            yield item


if __name__ == '__main__':
    print(list(chain([1, 2, 3], [4, 5, 6])))
    a = chain([1, 2, 3], [4, 5, 6])
    print(a)
    # print(a[5])
    from collections import Iterable
    print(isinstance(a, Iterable))
    # print(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])))
