import json
import sys


def map_skill_best_person(people):
    skill_best = {}
    for person in people:
        person_name = f'{person["first_name"]} {person["last_name"]}'
        for skill in person['skills']:
            if (skill['name'] not in skill_best or (skill['name'] in skill_best
               and skill['level'] > skill_best[skill['name']][1])):
                skill_best[skill['name']] = (person_name, skill['level'])
    return skill_best


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        data = json.load(f)
    for language, person in map_skill_best_person(data['people']).items():
        print(f'{language} - {person[0]}')
