import csv

FILE__NAME = 'example_data.csv'


def comare_strings_or_numbers_bigger(string1, string2):
    import re
    number_re = re.compile(r'(\d+$)|(\d+.\d+$)')
    if number_re.match(string1) is None or number_re.match(string2) is None:
        return string1 > string2
    return float(string1) > float(string2)


def cut_special_ending(key):
    import re
    special_endings = ['__startswith', '__contains', '__gt', '__lt']
    for ending in special_endings:
        if key.endswith(ending):
            return re.sub(ending, '', key)
    return key


def generate_special_check(key_word, factor):
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
    for key, factor in factors.items():
        key_word = cut_special_ending(key)
        if (key_word not in person.keys() or (key_word in person.keys() and
           generate_special_check(key, factor)(person[key_word]) is False)):
            return None
    return person


def order_by(people, key):
    for i in range(0, len(people) - 1):
        for j in range(i, len(people)):
            if comare_strings_or_numbers_bigger(people[i][key],
                                                people[j][key]):
                people[i], people[j] = people[j], people[i]
    return people


def filter_people(people, **factors):
    filtered_people = []
    for person in people:
        checked_person = check_one_person(person, **factors)
        if checked_person is not None:
            filtered_people.append(checked_person)
    return filtered_people


def format_person(person):
    next_line = ''
    for value in person.values():
        if ',' in value:
            next_line = f'{next_line},\"{value}\"'
        else:
            next_line = f'{next_line},{value}'
    return next_line.replace(',', '', 1)


def format_people(people):
    final_string = ''
    for person in people:
        final_string = f'{final_string}{format_person(person)}\n'
    return final_string


def filter(file_name, **factors):
    order = factors.pop('order_by', False)
    with open(FILE__NAME, 'r') as csv_file:
        people = csv.DictReader(csv_file)
        filtered_people = filter_people(people, **factors)
    if order is not False:
        filtered_people = order_by(filtered_people, order)
        factors['order_by'] = order
    return filtered_people


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
            final_string = f'{final_string},{column_name}'
        final_string = final_string.replace(',', '', 1)
        final_string = f'{final_string}\n{format_people(people)}\n'
        f.write(final_string)
        return final_string


if __name__ == '__main__':
    people = filter(FILE__NAME, salary__gt='9931', order_by='salary')
    make_csv_file('example_data_filtered.csv', people)
