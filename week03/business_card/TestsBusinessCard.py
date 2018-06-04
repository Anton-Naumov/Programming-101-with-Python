import unittest
import textwrap

from BusinessCard import (css_file, generate_head_tag, create_interests_tag,
                          create_skills_tag, generate_tag,
                          create_base_info_tag, generate_one_word_tag)


class Test_Business_Card(unittest.TestCase):
    def test_generate_head_tag_random_name(self):
        expected_output = textwrap.dedent(f"""\
        <head>
          <title>Ivo Ivo</title>
          <link rel="stylesheet" type="text/css" href="{css_file}">
        </head>""")
        self.assertEqual(generate_head_tag('Ivo Ivo'), expected_output)

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

    def test_generate_tag_with_empty_content(self):
        _type = 'body'
        name = 'Every day'
        content = []
        expected_output = textwrap.dedent("""\
        <body class="Every day">
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

    def test_generate_one_word_tag_empty_name(self):
        self.assertEqual(generate_one_word_tag('li', '', 'eating'),
                         '<li>eating</li>')
        self.assertEqual(generate_one_word_tag('li', '', 'sleeping'),
                         '<li>sleeping</li>')

    def test_generate_one_word_tag_random_words(self):
        self.assertEqual(generate_one_word_tag('li', 'morning', 'eating'),
                         '<li class="morning">eating</li>')
        self.assertEqual(generate_one_word_tag('li', 'evening', 'sleeping'),
                         '<li class="evening">sleeping</li>')

    def test_generate_interests_tag_empty_interests(self):
        self.assertEqual(create_interests_tag([]),
                         textwrap.dedent("""\
                         <div class="interests">
                           <h2>Interests:</h2>
                           <ul>
                           </ul>
                         </div>"""))

    def test_generate_interests_tag_with_interests(self):
        self.assertEqual(create_interests_tag(['eating', 'sleeping']),
                         textwrap.dedent("""\
                         <div class="interests">
                           <h2>Interests:</h2>
                           <ul>
                             <li>eating</li>
                             <li>sleeping</li>
                           </ul>
                         </div>"""))

    def test_generate_skills_tag_empty_skills(self):
        self.assertEqual(create_skills_tag([]),
                         textwrap.dedent("""\
                         <div class="skill">
                           <h2>Skills:</h2>
                           <ul>
                           </ul>
                         </div>"""))

    def test_generate_skills_tag_with_skills(self):
        skills = [{
            "name": "C++",
            "level": 30
        }, {
            "name": "PHP",
            "level": 25
        }]
        self.assertEqual(create_skills_tag(skills),
                         textwrap.dedent("""\
                         <div class="skill">
                           <h2>Skills:</h2>
                           <ul>
                             <li>C++ - 30</li>
                             <li>PHP - 25</li>
                           </ul>
                         </div>"""))

    def test_generate_base_info_tag_with_only_exceptions_in_person(self):
        person = {
            "first_name": "Ivo",
            "last_name": "Ivo",
            "gender": "male",
            "interests": ["eating", "sleeping", "programming", "skiing"],
            "avatar": "ivo.png",
            "skills": [{
                "name": "C++",
                "level": 30
            }]
        }
        self.assertEqual(create_base_info_tag(person),
                         textwrap.dedent("""\
                         <div class="base-info">
                         </div>"""))

    def test_generate_base_info_tag(self):
        person = {
            "first_name": "Ivo",
            "last_name": "Ivo",
            "age": 25,
            "birth_date": "05/05/2005",
            "birth_place": "Sofia",
            "gender": "male",
        }
        self.assertEqual(create_base_info_tag(person),
                         textwrap.dedent("""\
                         <div class="base-info">
                           <p>age: 25</p>
                           <p>birth_date: 05/05/2005</p>
                           <p>birth_place: Sofia</p>
                         </div>"""))


if __name__ == '__main__':
    unittest.main()
