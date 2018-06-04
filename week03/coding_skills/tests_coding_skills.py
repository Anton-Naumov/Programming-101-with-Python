import unittest

from coding_skills import (add_person_if_better, get_best_people,
                           format_best_people)


class TestsCodingSkills(unittest.TestCase):
    def setUp(self):
        self.best_people = {'C++': {'name': 'Pesho Pesho', 'level': 100},
                            'Java': {'name': 'Reni Reni', 'level': 100},
                            'Python': {'name': 'Sasho Sasho', 'level': 100}}

    def test_add_person_if_better_not_better_in_any_skill(self):
        person = {
            "first_name": "Ivo",
            "last_name": "Ivo",
            "skills": [{
                "name": "C++",
                "level": 30
            }, {
                "name": "Python",
                "level": 80
            }, {
                "name": "Java",
                "level": 25
            }]}
        self.assertEqual(add_person_if_better(person, self.best_people),
                         {'C++': {'name': 'Pesho Pesho',
                                  'level': 100},
                          'Java': {'name': 'Reni Reni',
                                   'level': 100},
                          'Python': {'name': 'Sasho Sasho',
                                     'level': 100}})

    def test_add_person_if_better_add_skills_if_they_dont_exist(self):
        person = {
            "first_name": "Rado",
            "last_name": "Rado",
            "skills": [{
                "name": "PHP",
                "level": 37
            }, {
                "name": "Haskell",
                "level": 70
            }]}
        self.assertEqual(add_person_if_better(person, self.best_people),
                         {'C++': {'name': 'Pesho Pesho',
                                  'level': 100},
                          'Java': {'name': 'Reni Reni',
                                   'level': 100},
                          'Python': {'name': 'Sasho Sasho',
                                     'level': 100},
                          'PHP': {'name': 'Rado Rado',
                                  'level': 37},
                          'Haskell': {'name': 'Rado Rado',
                                      'level': 70}})

    def test_add_person_if_better_empty_best_people(self):
        person = {
            "first_name": "Toni",
            "last_name": "Toni",
            "skills": [{
                "name": "C++",
                "level": 150
            }]}
        self.assertEqual(add_person_if_better(person, {}), {'C++': {
                                                        'name': 'Toni Toni',
                                                        'level': 150}})

    def test_add_person_if_better_change_in_all_skills_better_in(self):
        person = {
            "first_name": "Ceco",
            "last_name": "Ceco",
            "skills": [{
                "name": "C++",
                "level": 120
            }, {
                "name": "Python",
                "level": 95
            }, {
                "name": "Java",
                "level": 135
            }]}
        self.assertEqual(add_person_if_better(person, self.best_people),
                         {'C++': {'name': 'Ceco Ceco',
                                  'level': 120},
                          'Java': {'name': 'Ceco Ceco',
                                   'level': 135},
                          'Python': {'name': 'Sasho Sasho',
                                     'level': 100}})

    def test_get_best_people_with_multiple_people(self):
        people = [{
            "first_name": "Ivo",
            "last_name": "Ivo",
            "skills": [{
                "name": "C++",
                "level": 30
            }, {
                "name": "PHP",
                "level": 25
            }]
        }, {
            "first_name": "Rado",
            "last_name": "Rado",
            "skills": [{
                "name": "C++",
                "level": 20
            }, {
                "name": "Python",
                "level": 10
            }, {
                "name": "JavaScript",
                "level": 60
            }]
        }, {
            "first_name": "Magi",
            "last_name": "Magi",
            "skills": [{
                "name": "JavaScript",
                "level": 59
            }, {
                "name": "Python",
                "level": 66
            }, {
                "name": "Ruby",
                "level": 37
            }]
        }]
        self.assertEqual(get_best_people(people),
                         {'C++': {'name': 'Ivo Ivo',
                                  'level': 30},
                          'PHP': {'name': 'Ivo Ivo',
                                  'level': 25},
                          'Python': {'name': 'Magi Magi',
                                     'level': 66},
                          'JavaScript': {'name': 'Rado Rado',
                                         'level': 60},
                          'Ruby': {'name': 'Magi Magi',
                                   'level': 37}})

    def test_format_best_people_empty_best_people(self):
        self.assertEqual(format_best_people({}), '')

    # def test_format_best_people_with_three_people(self):
    #     self.assertEqual(format_best_people(self.best_people),
    #                      'C++ - Pesho Pesho\n'
    #                      'Java - Reni Reni\n'
    #                      'Python - Sasho Sasho\n')


if __name__ == '__main__':
    unittest.main()
