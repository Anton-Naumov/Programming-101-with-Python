import unittest
import textwrap

from BusinessCard import (css_file, generate_head_tag,
                          validate_generate_tag_arguments, generate_tag,
                          generate_one_word_tag, validate_interests,
                          validate_skills, validate_person)


class Test_Business_Card(unittest.TestCase):
    def test_generate_head_tag_non_string_argument(self):
        with self.assertRaises(TypeError):
            generate_head_tag(123)

    def test_generate_head_tag_random_name(self):
        expected_output = textwrap.dedent(f"""\
        <head>
          <title>Ivo Ivo</title>
          <link rel="stylesheet" type="text/css" href="{css_file}">
        </head>""")
        self.assertEqual(generate_head_tag('Ivo Ivo'), expected_output)

    def test_validate_generate_tag_arguments_non_string_type_or_name(self):
        with self.assertRaises(TypeError):
            validate_generate_tag_arguments(123, 'Interests', [''])
        with self.assertRaises(TypeError):
            validate_generate_tag_arguments('body', 123, [''])

    def test_validate_generate_tag_arguments_non_list_content(self):
        with self.assertRaises(TypeError):
            validate_generate_tag_arguments('body', 'Interests', 'content')

    def test_validate_generate_tag_arguments_non_string_content_element(self):
        with self.assertRaises(TypeError):
            validate_generate_tag_arguments('body', 'Interests',
                                            ['Anton', 12345])

    def test_test_generate_tag_with_empty_name(self):
        _type = 'body'
        name = ''
        content = ['eating', 'sleaping', 'programing']
        expected_output = textwrap.dedent("""\
        <body>
          eating
          sleaping
          programing
        </body>""")
        self.assertEqual(generate_tag(_type, name, content), expected_output)

    def test_generate_tag_with_simple_content(self):
        _type = 'body'
        name = 'Every day'
        content = ['eating', 'sleaping', 'programing']
        expected_output = textwrap.dedent("""\
        <body class="Every day">
          eating
          sleaping
          programing
        </body>""")
        self.assertEqual(generate_tag(_type, name, content), expected_output)

    def test_generate_tag_with_complex_content(self):
        sub_tage_type = 'body'
        sub_tag_name = 'Every day'
        sub_tag_ontent = ['eating', 'sleaping', 'programing']
        sub_tag = generate_tag(sub_tage_type, sub_tag_name, sub_tag_ontent)

        tag_type = 'div'
        tag_name = 'Anton'
        tag_content = ['Hack Bulgaria', 'Python', sub_tag]

        expected_output = textwrap.dedent("""\
        <div class="Anton">
          Hack Bulgaria
          Python
          <body class="Every day">
            eating
            sleaping
            programing
          </body>
        </div>""")
        self.assertEqual(generate_tag(tag_type, tag_name, tag_content),
                         expected_output)

    def test_generate_one_word_tag_non_string_arguments(self):
        with self.assertRaises(TypeError):
            generate_one_word_tag(123, 'name', 'word')
        with self.assertRaises(TypeError):
            generate_one_word_tag('type', 123, 'word')
        with self.assertRaises(TypeError):
            generate_one_word_tag('type', 'name', 123)

    def test_generate_one_word_tag_random_words(self):
        self.assertEqual(generate_one_word_tag('li', 'morning', 'eating'),
                         '<li class="morning">eating</li>')
        self.assertEqual(generate_one_word_tag('li', 'evening', 'sleeping'),
                         '<li class="evening">sleeping</li>')

    def test_validate_interests_not_list(self):
        with self.assertRaises(TypeError):
            validate_interests("string")

    def test_validate_interests_non_string_element(self):
        with self.assertRaises(TypeError):
            validate_interests(['programing', 123])

    def test_validate_skills_non_list(self):
        with self.assertRaises(TypeError):
            validate_skills('non list')

    def test_validate_skills_non_dict_element(self):
        with self.assertRaises(TypeError):
            validate_skills([{'name': 'C++', 'level': 100}, 'non dict'])

    def test_validate_skills_non_skill_with_no_name_or_level(self):
        with self.assertRaises(ValueError):
            validate_skills([{'name': 'C++', 'level': 100}, {'level': 10}])
        with self.assertRaises(ValueError):
            validate_skills([{'name': 'Java'}, {'name': 'C++', 'level': 100}])

    def test_validate_person_with_no_first_or_last_name_or_skills(self):
        with self.assertRaises(ValueError):
            validate_person({
                    "last_name": "Ivo",
                    "interests": ['eating'],
                    "gender": 'male',
                    "skills": [{
                        "name": "C++",
                        "level": 30
                    }]})
        with self.assertRaises(ValueError):
            validate_person({
                    "first_name": "Ivo",
                    "interests": ['eating'],
                    "gender": 'male',
                    "skills": [{
                        "name": "C++",
                        "level": 30
                    }]})
        with self.assertRaises(ValueError):
            validate_person({
                    "first_name": "Ivo",
                    "last_name": "Ivo",
                    "interests": ['eating'],
                    "gender": 'male',
                    })

    def test_validate_person_with_no_interests_or_gender(self):
        with self.assertRaises(ValueError):
            validate_person({
                    "first_name": "Ivo",
                    "last_name": "Ivo",
                    "gender": 'male',
                    "skills": [{
                        "name": "C++",
                        "level": 30
                    }]})
        with self.assertRaises(ValueError):
            validate_person({
                    "first_name": "Ivo",
                    "last_name": "Ivo",
                    "interests": ['eating'],
                    "skills": [{
                        "name": "C++",
                        "level": 30
                    }]})


if __name__ == '__main__':
    unittest.main()
