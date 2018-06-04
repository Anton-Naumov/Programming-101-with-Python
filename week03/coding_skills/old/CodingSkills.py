import json
import sys


def format_full_name(first_name, second_name):
    if (type(first_name) is not str or type(second_name) is not str):
        raise TypeError("Names should be stings!")
    return f'{first_name} {second_name}'


def validate_skill(skill):
    if (len(skill.keys()) != 2 or 'name' not in skill or 'level' not in skill):
        raise ValueError('All skills must have name and level!')
    if (type(skill['name']) is not str or type(skill['level']) is not int):
        raise TypeError("Ivalid skill name or level!")


def map_skill_name_to_level(skills):
    if type(skills) is not list:
        raise TypeError("Skills type not a list!")
    name_level_dict = {}
    for skill in skills:
        validate_skill(skill)
        name_level_dict[skill['name']] = skill['level']
    return name_level_dict


def validate_person(person):
    if (type(person) is not dict or len(person.keys()) is not 3 or
        'first_name' not in person or 'last_name' not in person or
       'skills' not in person):
        raise ValueError("Invalid person data")


def get_skill_best_person_dict(people):
    if type(people) is not list:
        return TypeError("The people argument should be a list!")
    skill_best = {}
    for person in people:
        validate_person(person)
        name = format_full_name(person['first_name'], person['last_name'])
        for skill, level in map_skill_name_to_level(person['skills']).items():
            if (skill not in skill_best or
               (skill in skill_best and level > skill_best[skill]['level'])):
                skill_best[skill] = {'name': name, 'level': level}
    return skill_best


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        data = json.load(f)
