import re


def extract_variable_and_power(string):
    parts = string.split('^')

    if re.match(r'[a-z]$', parts[0]):
        if len(parts) == 1:
            return parts[0], 1

        if len(parts) == 2 and parts[1].isdigit():
            return parts[0], int(parts[1])

    raise Exception('Invalid string!')


def extract_term(string):
    parts = string.split('*')

    if len(parts) == 1:
        if parts[0].isdigit():
            return int(parts[0]), 'x', 0
        else:
            return (1, *extract_variable_and_power(parts[0]))

    if len(parts) == 2 and parts[0].isdigit():
        return (int(parts[0]), *extract_variable_and_power(parts[1]))

    raise Exception('Invalid string!')
