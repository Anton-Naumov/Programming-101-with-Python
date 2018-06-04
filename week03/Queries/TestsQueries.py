import unittest

from collections import OrderedDict
from Queries import (check_one_person, generate_special_check,
                     comare_strings_or_numbers_bigger, cut_special_ending,
                     order_by, filter_people, format_person, format_people)


class TestsQueries(unittest.TestCase):
    def setUp(self):
        self.person1 = {'full_name': 'Anton', 'salary': '200.75',
                        'height': '190', 'favorite_color': 'blue'}
        self.person2 = {'full_name': 'Roni', 'salary': '1000',
                        'height': '150', 'favorite_color': 'green'}
        self.person3 = {'full_name': 'Vasko', 'salary': '1000.25',
                        'height': '190', 'favorite_color': 'blue'}
        self.person4 = {'full_name': 'Sully', 'salary': '5500',
                        'height': '179', 'favorite_color': 'brown'}
        self.people = [self.person1, self.person2, self.person3, self.person4]

    def test_comare_strings_or_numbers_bigger_no_number_in_string(self):
        self.assertEqual(comare_strings_or_numbers_bigger('aaa', 'b'), False)
        self.assertEqual(comare_strings_or_numbers_bigger('b', 'anton'), True)
        self.assertEqual(comare_strings_or_numbers_bigger('a', 'a'), False)

    def test_comare_strings_or_numbers_bigger_with_integers_in_strings(self):
        self.assertEqual(comare_strings_or_numbers_bigger('500', '450'), True)
        self.assertEqual(comare_strings_or_numbers_bigger('450', '500'), False)

    def test_comare_strings_or_numbers_bigger_with_one_number_string(self):
        self.assertEqual(comare_strings_or_numbers_bigger('500', 'a'), False)
        self.assertEqual(comare_strings_or_numbers_bigger('a', '500'), True)

    def test_comare_strings_or_numbers_bigger_with_strings_with_float(self):
        self.assertEqual(comare_strings_or_numbers_bigger('2.50', '10'), False)
        self.assertEqual(comare_strings_or_numbers_bigger('10', '2.50'), True)
        self.assertEqual(comare_strings_or_numbers_bigger('10.7', '2.5'), True)

    def test_cut_special_ending_no_special_ending(self):
        self.assertEqual(cut_special_ending('phone_number'), 'phone_number')
        self.assertEqual(cut_special_ending('salary'), 'salary')

    def test_cut_special_ending_test_random_special_endings(self):
        self.assertEqual(cut_special_ending('full_name__startswith'),
                         'full_name')
        self.assertEqual(cut_special_ending('salary__gt'),
                         'salary')
        self.assertEqual(cut_special_ending('phone_number__contains'),
                         'phone_number')
        self.assertEqual(cut_special_ending('age__lt'),
                         'age')

    def test_check_one_person_with_non_existing_factor_key(self):
        person = OrderedDict([('full_name', 'Anton'), ('salary', '5000')])
        self.assertEqual(check_one_person(person, favorite_color='green'),
                         None)

    def test_check_one_person_simple_tests(self):
        person1 = OrderedDict([('full_name', 'Anton')])
        person2 = OrderedDict([('full_name', 'Anton'),
                               ('favorite_color', 'blue'),
                               ('phone_number', '114-116-1124x315')])
        self.assertEqual(check_one_person(person1, full_name='Anton'), person1)
        self.assertEqual(check_one_person(person1, full_name='Vasko'), None)
        self.assertEqual(check_one_person(person2, full_name='Anton',
                         favorite_color='blue'), person2)
        self.assertEqual(check_one_person(person2, full_name='Anton',
                         favorite_color='green'), None)

    def test_check_one_person_tests_with_special_ending(self):
        person1 = OrderedDict([('full_name', 'Anton')])
        person2 = OrderedDict([('full_name', 'Anton'),
                               ('favorite_color', 'blue'),
                               ('phone_number', '114-116-1124x315'),
                               ('salary', '5000')])
        self.assertEqual(check_one_person(person1, full_name__startswith='A'),
                         person1)
        self.assertEqual(check_one_person(person1, full_name__startswith='P'),
                         None)
        self.assertEqual(check_one_person(person2,
                         phone_number__contains='x'),
                         person2)
        self.assertEqual(check_one_person(person2, salary__lt='4000'),
                         None)
        self.assertEqual(check_one_person(person2, salary__gt='4000'),
                         person2)
        self.assertEqual(check_one_person(person2, full_name__contains='nto'),
                         person2)

    def test_generate_special_check_key_word_ending_with__startswith(self):
        func_generated = generate_special_check('full_name__startswith',
                                                'Diana')
        self.assertEqual(func_generated('Diana Dianova'), True)
        self.assertEqual(func_generated('Doni Petrova Diana'), False)
        self.assertEqual(func_generated('Diananita Georgieva'), True)
        self.assertEqual(func_generated('Monica-Diana Peshova'), False)
        self.assertEqual(func_generated('Pesho Kirov'), False)

    def test_generate_special_check_key_word_ending_with__contains(self):
        func_generated = generate_special_check('full_name__contains', 'Diana')
        self.assertEqual(func_generated('Diana Dianova'), True)
        self.assertEqual(func_generated('Doni Petrova Diana'), True)
        self.assertEqual(func_generated('Diananita Georgieva'), True)
        self.assertEqual(func_generated('Monica-Diana Peshova'), True)
        self.assertEqual(func_generated('Pesho Kirov'), False)

    def test_generate_special_check_key_word_end_with__gt_with_numbers(self):
        func_generated = generate_special_check('salary__gt', '1000')
        with self.assertRaises(TypeError):
            func_generated(123)
        self.assertEqual(func_generated('1200'), True)
        self.assertEqual(func_generated('1000.50'), True)
        self.assertEqual(func_generated('900'), False)

    def test_generate_special_check_key_word_end_with__lt_with_numbers(self):
        func_generated = generate_special_check('salary__lt', '1000')
        with self.assertRaises(TypeError):
            func_generated(123)
        self.assertEqual(func_generated('1200'), False)
        self.assertEqual(func_generated('1000.50'), False)
        self.assertEqual(func_generated('900'), True)

    def test_generate_special_check_key_word_with_no_special_ending(self):
        func_generated = generate_special_check('full_name', 'Anton')
        self.assertEqual(func_generated('Anton'), True)
        self.assertEqual(func_generated('Vasko'), False)

    def test_order_by_with_empty_people_list(self):
        self.assertEqual(order_by([], 'full_name'), [])

    def test_order_by_ordered_people(self):
        self.assertEqual(order_by([self.person2, self.person3, self.person1],
                                  'height'),
                         [self.person2, self.person3, self.person1])
        self.assertEqual(order_by([self.person1, self.person2, self.person3],
                                  'salary'),
                         [self.person1, self.person2, self.person3])

    def test_order_by_mixed_people(self):
        self.assertEqual(order_by([self.person2, self.person3, self.person1],
                                  'full_name'),
                         [self.person1, self.person2, self.person3])
        self.assertEqual(order_by([self.person3, self.person2, self.person1],
                                  'salary'),
                         [self.person1, self.person2, self.person3])

    def test_filter_people_without_people(self):
        self.assertEqual(filter_people([], full_name_startswith='A'), [])

    def test_filter_people_with_no_matches(self):
        self.assertEqual(filter_people(self.people, full_name='Danny'), [])
        self.assertEqual(filter_people(self.people, salary__gt='7000'), [])

    def test_filter_people_with_matches(self):
        self.assertEqual(filter_people(self.people, favorite_color='blue',
                                       height='190'),
                         [self.person1, self.person3])
        self.assertEqual(filter_people(self.people, salary__lt='10000'),
                         self.people)
        self.assertEqual(filter_people(self.people, full_name__startswith='R'),
                         [self.person2])
        self.assertEqual(filter_people(self.people, full_name__contains='ll'),
                         [self.person4])

    def test_format_person_empty_person(self):
        self.assertEqual(format_person({}), '')

    def test_format_person_with_a_field_that_has_comma_in_it(self):
        person = {'full_name': 'Sully', 'salary': '5500',
                  'home_town': 'Las Vegas, California'}
        self.assertEqual(format_person(person),
                         'Sully,5500,"Las Vegas, California"')

    def test_format_person_without_commas_in_filds(self):
        self.assertEqual(format_person(self.person1),
                         'Anton,200.75,190,blue')

    def test_format_peole_no_people(self):
        self.assertEqual(format_people([]), '')

    def test_format_peole_with_people(self):
        self.assertEqual(format_people(self.people),
                         'Anton,200.75,190,blue\n'
                         'Roni,1000,150,green\n'
                         'Vasko,1000.25,190,blue\n'
                         'Sully,5500,179,brown\n')


if __name__ == '__main__':
    unittest.main()
