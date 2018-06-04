import sys
import json


def add_person_if_better(person, best_people):
    for skill in person['skills']:
        formated_name = f'{person["first_name"]} {person["last_name"]}'
        if (skill['name'] not in best_people or
           (skill['name'] in best_people and
           skill['level'] > best_people[skill['name']]['level'])):
            best_people[skill['name']] = {'name': formated_name,
                                          'level': skill['level']}
    return best_people


def get_best_people(people):
    best_people = {}
    for person in people:
        add_person_if_better(person, best_people)
    return best_people


def format_best_people(best_people):
    result = ''
    for skill_name, person in best_people.items():
        result = f'{result}{skill_name} - {person["name"]}\n'
    return result


def open_file(file_name):
    with open(file_name, 'r') as f:
        return json.load(f)


if __name__ == '__main__':
    people = open_file(sys.argv[1])
    best_people = get_best_people(people['people'])
    print(format_best_people(best_people))
