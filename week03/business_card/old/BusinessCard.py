import json
import sys
import textwrap

css_file = "styles.css"


def generate_head_tag(name):
    if type(name) is not str:
        raise TypeError('The head tag name must be a string!')
    return textwrap.dedent(f"""\
            <head>
              <title>{name}</title>
              <link rel="stylesheet" type="text/css" href="{css_file}">
            </head>""")


def validate_generate_tag_arguments(_type, name, content):
    if type(_type) is not str or type(name) is not str:
        raise TypeError('The tag type and name must be strings!')
    if type(content) is not list:
        raise TypeError('The content argument must be a list!')
    for data in content:
        if type(data) is not str:
            raise TypeError("All of the contents must be strings!")


def generate_tag(_type, name, content):
    validate_generate_tag_arguments(_type, name, content)
    if name != '':
        result_string = f'<{_type} class="{name}">'
    else:
        result_string = f'<{_type}>'
    for data in content:
        data_lines = data.split('\n')
        for line in data_lines:
            result_string = f'{result_string}\n  {line}'
    result_string = f'{result_string}\n</{_type}>'
    return result_string


def generate_one_word_tag(_type, name, word):
    if (type(_type) is not str or type(name) is not str or
       type(word) is not str):
        raise TypeError("The _type and word must be strings!")
    if name == '':
        return f'<{_type}>{word}</{_type}>'
    else:
        return f'<{_type} class="{name}">{word}</{_type}>'


def validate_interests(interests):
    if type(interests) is not list:
        raise TypeError("The interests must be a list with strings!")
    for interest in interests:
        if type(interest) is not str:
            raise TypeError("All interests must be string!")


def validate_skills(skills):
    if type(skills) is not list:
        raise TypeError("The skills must be a list with dictionaries!")
    for skill in skills:
        if type(skill) is not dict:
            raise TypeError("Every skill must be a dictionaries!")
        if ('name' not in skill or 'level' not in skill or
           len(skill.keys()) != 2):
            raise ValueError("Every skill must have a name and a level only!")


def validate_person(person):
    if type(person) is not dict:
        raise TypeError("The person must be a dictionarie!")
    if 'first_name' not in person or 'last_name' not in person:
        raise ValueError("The person must hava first name and last name!")
    if 'interests' not in person or 'skills' not in person:
        raise ValueError("The person must have interest and skills!")
    if 'avatar' not in person or 'gender' not in person:
        raise ValueError("The person must have interest and skills!")
    validate_interests(person['interests'])
    validate_skills(person['skills'])


def create_interests_tag(interests):
    validate_interests(interests)
    interest_header = generate_one_word_tag('h2', '', 'Interests:')
    interests_list = []
    for interest in interests:
        interests_list.append(generate_one_word_tag('li', '', interest))
    return generate_tag('div', 'interests', [interest_header,
                        generate_tag('ul', '', interests_list)])


def create_skills_tag(skills):
    validate_skills(skills)
    skill_header = generate_one_word_tag('h2', '', 'Skills:')
    skill_list = []
    for skill in skills:
        skill_list.append(generate_one_word_tag('li', '',
                          f'{skill["name"]} - {skill["level"]}'))
    return generate_tag('div', 'skill', [skill_header,
                        generate_tag('ul', '', skill_list)])


def create_base_info_tag(person):
    validate_person(person)
    exceptions = ['first_name', 'last_name', 'interests', 'skills', 'avatar',
                  'gender']
    base_list = []
    for key, value in person.items():
        if key not in exceptions:
            base_list.append(generate_one_word_tag('p', '', f'{key}: {value}'))
    return generate_tag('div', 'base-info', base_list)


def get_person_business_card(person):
    validate_person(person)
    h_tag = generate_head_tag(f'{person["first_name"]} {person["last_name"]}')
    full_name = f'{person["first_name"]} {person["last_name"]}'
    full_name_tag = generate_one_word_tag('h1', 'full-name', full_name)
    avatar_tag = '<img class="avatar" src="avatars/%s">' % (person["avatar"])
    interest_tag = create_interests_tag(person['interests'])
    skill_tag = create_skills_tag(person['skills'])
    base_info_tag = create_base_info_tag(person)
    big_div_content = [full_name_tag, avatar_tag, base_info_tag,
                       interest_tag, skill_tag]
    big_div_tag = generate_tag('div', f'business-card {person["gender"]}',
                               big_div_content)
    body_tag = generate_tag('body', '', [big_div_tag])
    html_tag = generate_tag('html', '', [h_tag, body_tag])
    return html_tag


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        data = json.load(f)
    get_person_business_card(data['people'][0])
    for person in data['people']:
        validate_person(person)
        output_file_name = f'{person["first_name"]}_{person["last_name"]}.html'
        with open(output_file_name, 'w') as f:
            f.write(get_person_business_card(person))
