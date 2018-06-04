import unittest

from codingSkills import map_skill_best_person

simple_test_list = [{
        "first_name": "Ivo",
        "last_name": "Ivo",
        "skills": [{
            "name": "C++",
            "level": 30
        }]}]

simple_test_list_result = {'C++': ('Ivo Ivo', 30)}

dict_with_two_people = [{
        "first_name": "Ivo",
        "last_name": "Ivo",
        "skills": [{
            "name": "C++",
            "level": 30
        }, {
            "name": "PHP",
            "level": 25
        }, {
            "name": "Python",
            "level": 80
        }, {
            "name": "C#",
            "level": 25
        }]
    }, {
        "first_name": "Rado",
        "last_name": "Rado",
        "skills": [{
            "name": "C++",
            "level": 20
        }, {
            "name": "PHP",
            "level": 37
        }, {
            "name": "Haskell",
            "level": 70
        }, {
            "name": "Java",
            "level": 50
        }, {
            "name": "C#",
            "level": 10
        }, {
            "name": "JavaScript",
            "level": 60
        }]}]

dict_with_two_people_result = {'C++': ('Ivo Ivo', 30),
                               'PHP': ('Rado Rado', 37),
                               'Haskell': ('Rado Rado', 70),
                               'Java': ('Rado Rado', 50),
                               'C#': ('Ivo Ivo', 25),
                               'JavaScript': ('Rado Rado', 60),
                               'Python': ('Ivo Ivo', 80)}

dict_with_three_people = [{
        "first_name": "Ivo",
        "last_name": "Ivo",
        "skills": [{
            "name": "C++",
            "level": 30
        }]
    }, {
        "first_name": "Rado",
        "last_name": "Rado",
        "skills": [{
            "name": "C++",
            "level": 20
        }]
    },
        {
        "first_name": "Toni",
        "last_name": "Toni",
        "skills": [{
            "name": "C++",
            "level": 50
        }]}]


dict_with_three_people_result = {'C++': ('Toni Toni', 50)}


class Coding_Skills_Tests(unittest.TestCase):
    def test_map_skill_best_person_empty_list(self):
        self.assertEqual(map_skill_best_person([]), {})

    def test_map_skill_best_person_simple_test(self):
        self.assertEqual(map_skill_best_person(simple_test_list),
                         simple_test_list_result)

    def test_map_skill_best_person_two_people(self):
        self.assertEqual(map_skill_best_person(dict_with_two_people),
                         dict_with_two_people_result)
        self.assertEqual(map_skill_best_person(dict_with_three_people),
                         dict_with_three_people_result)


if __name__ == '__main__':
    unittest.main()
