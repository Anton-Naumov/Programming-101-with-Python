import csv
from collections import OrderedDict

FILE__NAME = 'example_data.csv'


def comare_strings_or_numbers_bigger(string1, string2):
    if type(string1) is not str or type(string2) is not str:
        raise TypeError('extract_number_from_string arguments must be string!')
    import re
    number_re = re.compile(r'(\d+$)|(\d+.\d+$)')
    if number_re.match(string1) is None or number_re.match(string2) is None:
        return string1 > string2
    return float(string1) > float(string2)


def cut_special_ending(key):
    import re
    if type(key) is not str:
        raise TypeError("The argument must be string!")
    special_endings = ['__startswith', '__contains', '__gt', '__lt']
    for ending in special_endings:
        if key.endswith(ending):
            return re.sub(ending, '', key)
    return key


def generate_special_check(key_word, factor):
    if type(key_word) is not str or type(factor) is not str:
        raise TypeError("Type of key word must be string!")
    if key_word.endswith('__startswith'):
        return lambda string: string.startswith(factor)
    if key_word.endswith('__contains'):
        return lambda string: factor in string
    if key_word.endswith('__gt'):
        return lambda string: comare_strings_or_numbers_bigger(string, factor)
    if key_word.endswith('__lt'):
        return lambda string: comare_strings_or_numbers_bigger(factor, string)
    return lambda string: string == factor


def check_one_person(person, **factors):
    if type(person) is not OrderedDict:
        raise TypeError("Type of the person must be ordered dict!")

    for key, factor in factors.items():
        if type(factor) is not str:
            raise TypeError("Type of all factors must be string!")
        key_word = cut_special_ending(key)
        if (key_word not in person.keys() or (key_word in person.keys() and
           generate_special_check(key, factor)(person[key_word]) is False)):
            return None

    return person


def filter(file_name, **factors):
    order = factors.pop('order_by', False)
    filt_p = []
    with open(FILE__NAME, 'r') as csv_file:
        people = csv.DictReader(csv_file)
        for person in people:
            checked_person = check_one_person(person, **factors)
            if checked_person is not None:
                filt_p.append(checked_person)
    if order is not False:
        for i in range(0, len(filt_p) - 1):
            for j in range(i, len(filt_p)):
                if comare_strings_or_numbers_bigger(filt_p[i][order],
                                                    filt_p[j][order]):
                    filt_p[i][order], filt_p[j][order] = (filt_p[j][order],
                                                          filt_p[i][order])
        factors['order_by'] = order
    make_csv_file(f'{file_name}_filtered.csv', filt_p)
    return filt_p


def count(file_name, **factors):
    return len(filter(file_name, **factors))


def first(file_name, **factors):
    return next(iter(filter(file_name, **factors)))


def last(file_name, **factors):
    return next(reversed(filter(file_name, **factors)))


def make_csv_file(file_name, people):
    with open(file_name, 'w') as f:
        if people is []:
            return ''
        final_string = ''
        for column_name in people[0].keys():
            final_string = f'{final_string}, {column_name}'
        final_string = final_string.replace(', ', '', 1)
        next_line = ''
        for person in people:
            for value in person.values():
                if ',' in value:
                    next_line = f'{next_line}, \"{value}\"'
                else:
                    next_line = f'{next_line}, {value}'
            next_line = next_line.replace(', ', '', 1)
            final_string = f'{final_string}\n{next_line}'
            next_line = ''
        f.write(final_string)
        return final_string


if __name__ == '__main__':
    filter(FILE__NAME, salary__gt='9925', order_by='salary')
    print(count(FILE__NAME, salary__gt='9925', order_by='salary'))
    print(first(FILE__NAME, salary__gt='9925', order_by='salary'))
    print(last(FILE__NAME, salary__gt='9925', order_by='salary'))
