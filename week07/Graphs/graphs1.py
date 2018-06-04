from collections import Iterable


def deep_find(data, key):
    assert isinstance(data, Iterable)

    for el in data:
        if isinstance(data, dict):
            if el == key:
                return data[el]
            elif isinstance(data[el], Iterable):
                el1 = deep_find(data[el], key)
                if el1 is not None:
                    return el1
        elif isinstance(el, Iterable):
            el1 = deep_find(el, key)
            if el1 is not None:
                return el1

    return None


def deep_find_all(data, key):
    assert isinstance(data, Iterable)

    result = []
    for el in data:
        if isinstance(data, dict):
            if el == key:
                result.append(data[el])
            elif isinstance(data[el], Iterable):
                result.extend(deep_find_all(data[el], key))
        elif isinstance(el, Iterable):
            result.extend(deep_find_all(el, key))

    return result


def deep_update(data, key, val):
    assert isinstance(data, Iterable)

    for el in data:
        if isinstance(data, dict):
            if el == key:
                data[el] = val
            elif isinstance(data[el], Iterable):
                deep_update(data[el], key, val)
        elif isinstance(el, Iterable):
            deep_update(el, key, val)


def deep_apply(func, data):
    if isinstance(data, dict):
        new_dict = {}
        for el in data:
            if isinstance(data[el], Iterable):
                deep_apply(func, data[el])
            new_dict[func(el)] = data[el]

        data.clear()
        data.update(new_dict)
    elif isinstance(data, Iterable):
        for el in data:
            if isinstance(el, Iterable) and not isinstance(el, str):
                deep_apply(func, el)
