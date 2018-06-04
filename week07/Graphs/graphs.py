from collections import Iterable
from copy import deepcopy


def deep_find(data, key):
    if isinstance(data, dict):
        for el in data:
            if el == key:
                return data[el]
            elif isinstance(data[el], Iterable):
                el1 = deep_find(data[el], key)
                if el1 is not None:
                    return el1
    elif isinstance(data, Iterable):
        for el in data:
            if isinstance(el, Iterable) and not isinstance(el, str):
                el1 = deep_find(el, key)
                if el1 is not None:
                    return el1

    return None


def deep_find_all(data, key):
    result = []
    if isinstance(data, dict):
        for el in data:
            if el == key:
                result.append(data[el])
            elif isinstance(data[el], Iterable):
                result.extend(deep_find_all(data[el], key))
    elif isinstance(data, Iterable):
        for el in data:
            if isinstance(el, Iterable) and not isinstance(el, str):
                result.extend(deep_find_all(el, key))

    return result


def deep_update(data, key, val):
    result = deepcopy(data)

    if isinstance(data, dict):
        for el in data:
            if el == key:
                result[el] = val
            else:
                result[el] = deep_update(data[el], key, val)
    elif isinstance(data, Iterable) and not isinstance(data, str):
        for i in range(len(data)):
            result[i] = deep_update(data[i], key, val)

    return result


def deep_apply(data, func):
    if isinstance(data, dict):
        new_data = {}
        for el in data:
            new_data[func(el)] = deep_apply(data[el], func)
    elif isinstance(data, Iterable) and not isinstance(data, str):
        new_data = deepcopy(data)
        for idx in range(len(data)):
            new_data[idx] = deep_apply(data[idx], func)
    else:
        return deepcopy(data)
    return new_data


def deep_compare(obj1, obj2):
    return obj1 == obj2


def schema_validator(schema: list, data: dict):
    if type(schema) is not list:
        raise Exception('Invalid schema!')
    if type(data) is not dict or len(data.keys()) != len(schema):
        return False

    for el in schema:
        if type(el) is list:
            if len(el) != 2:
                raise Exception('Invalid schema!')
            if el[0] not in data.keys() or not schema_validator(el[1], data[el[0]]):
                return False
        elif el not in data.keys():
            return False

    return True


data = {'a': [{'b': 2}, {'c': 3}, 'Anton'], 'c': 3}

data1 = {'lower_b': {'result': {'lower_c': 2, 'lower_d': 3, 'lower_inner': {'lower_inner_key': 42}}}}

schema = [
    'key1',
    'key2',
    [
        'key3',
        ['inner_key1', [
                            'inner_key2',
                            ['inner_inner_key1']
                       ]
         ]
    ]
]

data2 = {
    'key1': 'val1',
    'key2': 'val2',
    'key3': {
        'key2': 'val1',
        'inner_key2': {'key2': 5}
    }
}

data3 = {
    'key1': 'val1',
    'key2': 'val2',
    'key3': {
        'inner_key1': 'val1',
        'inner_key2': 'val2'
    },
    'key4': 'not expected'
}


def main():
    # data5 = [{'key2': 5, 'test': 10, 'a': [{'a': 10}]}, 'Anton']
    # new_data5 = deep_apply(lambda s: s.upper(), data5)
    # print(new_data5)
    # print(deep_find(data, 'c'))
    # print(deep_find(data1_f, 'c'))
    # print(deep_find_all(data, 'c'))
    # deep_update(data, 'c', 42)
    # print(data)
    # deep_apply(lambda key: f'{key}changed', data)
    # print(data)
    # deep_apply(lambda key: f'{key}changed', data1)
    # print(data1)
    # print(schema_validator(schema, data2))
    # print(schema_validator(schema, data3))
    print(deep_apply(data1, lambda s: s.upper()))
    print(deep_apply(data, lambda s: s.upper()))


if __name__ == '__main__':
    main()
