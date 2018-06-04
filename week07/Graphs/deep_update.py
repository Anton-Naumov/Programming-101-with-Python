from collections import Iterable


def deep_update(data, key, val):
    if isinstance(data, dict):
        for el in data:
            if el == key:
                data[el] = val
            elif isinstance(data[el], Iterable):
                deep_update(data[el], key, val)
    elif isinstance(data, Iterable):
        for el in data:
            if isinstance(el, Iterable) and not isinstance(el, str):
                deep_update(el, key, val)


if __name__ == '__main__':
    data = {
        'key': 5,
        'b': 10
    }

    deep_update(data, 'key', 42)

    print(data)
    print(data['key'] == 42)
