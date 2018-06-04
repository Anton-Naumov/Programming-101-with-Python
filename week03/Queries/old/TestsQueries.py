import unittest

from collections import OrderedDict
from Queries import (check_one_person, generate_special_check,
                     comare_strings_or_numbers_bigger, cut_special_ending)


class TestsQueries(unittest.TestCase):
    def test_comare_strings_or_numbers_bigger_no_string_argument(self):
        with self.assertRaises(TypeError):
            comare_strings_or_numbers_bigger(12345, '12345')
        with self.assertRaises(TypeError):
            comare_strings_or_numbers_bigger('12345', 12345)

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

    def test_cut_special_ending_non_string_argument(self):
        with self.assertRaises(TypeError):
            cut_special_ending(12345)

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

    def test_check_one_person_non_ordered_dict_person_argument(self):
        with self.assertRaises(TypeError):
            check_one_person('not ordered dict')

    def test_check_one_person_non_string_factor_value(self):
        person1 = OrderedDict([('full_name', 'Anton'), ('salary', '5000')])
        person2 = OrderedDict([('full_name', 'Anton'),
                               ('favorite_color', 'blue')])
        with self.assertRaises(TypeError):
            check_one_person(person1, full_name=123)
        with self.assertRaises(TypeError):
            check_one_person(person2, full_name='Anton', favorite_color=5)

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

    def test_generate_special_check_non_string_key_word_or_factor(self):
        with self.assertRaises(TypeError):
            generate_special_check(12345, 'factor')
        with self.assertRaises(TypeError):
            generate_special_check('key_word', 12345)

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


if __name__ == '__main__':
    unittest.main()
