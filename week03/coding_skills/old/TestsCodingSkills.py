import unittest

from CodingSkills import (format_full_name, map_skill_name_to_level,
                          validate_person, get_skill_best_person_dict)


class Test_Coding_Skills(unittest.TestCase):
    def test_format_full_name_non_string_arguments(self):
        with self.assertRaises(TypeError):
            format_full_name(123, "str")
        with self.assertRaises(TypeError):
            format_full_name("str", 123)

    def test_format_name_random_names(self):
        self.assertEqual(format_full_name('Ivo', 'Ivo'), 'Ivo Ivo')
        self.assertEqual(format_full_name('Anton', 'Naumov'), 'Anton Naumov')

    def test_map_skill_name_to_level_non_list_argument(self):
        with self.assertRaises(TypeError):
            map_skill_name_to_level({'name': 'C++', 'level': 10})

    def test_map_skill_name_to_level_unnamed_skill(self):
        skill_no_name = [{'name': 'C++', 'level': 10}, {'level': 15}]
        with self.assertRaises(ValueError):
            map_skill_name_to_level(skill_no_name)

    def test_map_skill_name_to_level_skill_with_no_level(self):
        skill_no_level = [{'name': 'Python'}, {'name': 'C++', 'level': 10}]
        with self.assertRaises(ValueError):
            map_skill_name_to_level(skill_no_level)

    def test_map_skill_name_to_level_skill_with_more_keys(self):
        with self.assertRaises(ValueError):
            map_skill_name_to_level([{'name': 'C++', 'level': 10, 'exp': 10}])

    def test_map_skill_name_to_level_non_string_name(self):
        with self.assertRaises(TypeError):
            map_skill_name_to_level([{'name': 123, 'level': 10}])

    def test_map_skill_name_to_level_non_int_level(self):
        with self.assertRaises(TypeError):
            map_skill_name_to_level([{'name': 'Python', 'level': '123'}])

    def test_map_skill_name_to_level_with_valid_argument(self):
        skills = [{'name': 'Python', 'level': 5}, {'name': 'C++', 'level': 10}]
        skills_return = {'Python': 5, 'C++': 10}
        self.assertEqual(map_skill_name_to_level(skills), skills_return)

    def test_validate_person_with_no_first_or_last_name_or_skills(self):
        with self.assertRaises(ValueError):
            validate_person({
                    "last_name": "Ivo",
                    "skills": [{
                        "name": "C++",
                        "level": 30
                    }]})
        with self.assertRaises(ValueError):
            validate_person({
                    "first_name": "Ivo",
                    "skills": [{
                        "name": "C++",
                        "level": 30
                    }]})
        with self.assertRaises(ValueError):
            validate_person([{
                    "first_name": "Ivo",
                    "last_name": "Ivo",
                    }])

    def test_get_skill_best_person_dict_one_person(self):
        one_person = [{
                "first_name": "Ivo",
                "last_name": "Ivo",
                "skills": [{
                    "name": "C++",
                    "level": 30
                }]}]
        one_person_result = {'C++': {'name': 'Ivo Ivo', 'level': 30}}
        self.assertEqual(get_skill_best_person_dict(one_person),
                         one_person_result)

    def test_get_skill_best_person_dict_three_people(self):
        three_people = [{
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
                }, {
                    "name": 'Python',
                    "level": 100
                }]}]
        three_people_result = {'C++': {'name': 'Toni Toni', 'level': 50},
                               'Python': {'name': 'Toni Toni', 'level': 100}}
        self.assertEqual(get_skill_best_person_dict(three_people),
                         three_people_result)


if __name__ == '__main__':
    unittest.main()
