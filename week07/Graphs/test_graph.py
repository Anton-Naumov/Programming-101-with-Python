import unittest
from graphs import deep_find, deep_find_all, deep_update, deep_apply


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.nested_dicts = {
            'a': {
                1,
                2
            },
            'b': {
                'apple': 3,
                'd': {
                    'apple': 5
                }
            },
            'apple': 42
        }

        self.dict_with_nested_lists = {'a': [[[{'b': 2}, {'apple': 42}]]], 'apple': 3}

        self.list_with_dicts = [{}, {'apple': 42}, 'Anton']

    def test_deep_find_with_nested_dicts(self):
        with self.subTest('With element on first level of nesting!'):
            nested_dicts = {
                'a': {
                    1,
                    2
                },
                'b': {
                    'c': 3,
                    'd': {
                        'g': 5
                    }
                },
                'apple': 42
            }

            self.assertEqual(
                deep_find(nested_dicts, 'apple'),
                42
            )

        with self.subTest('With element on third level of nesting!'):
            nested_dicts = {
                'a': {
                    1,
                    2
                },
                'b': {
                    'c': 3,
                    'd': {
                        'apple': 42
                    }
                },
                'c': 3
            }

            self.assertEqual(
                deep_find(nested_dicts, 'apple'),
                42
            )

    def test_deep_find_dict_with_nested_lists(self):
        dict_with_nested_lists = {'a': [[[{'b': 2}, {'apple': 42}]]], 'c': 3}

        self.assertEqual(
            deep_find(dict_with_nested_lists, 'apple'),
            42
        )

    def test_deep_find_list_with_dicts(self):
        list_with_dicts = [{}, {'apple': 42}, 'Anton']

        self.assertEqual(
            deep_find(list_with_dicts, 'apple'),
            42
        )

    def test_deep_find_finds_nothing(self):
        list_with_dicts = [{}, {'apple': 42}, 'Anton']

        self.assertEqual(
            deep_find(list_with_dicts, 'pineaplle'),
            None
        )

    def test_deep_find_all_with_nested_dicts(self):
        result_list = deep_find_all(self.nested_dicts, 'apple')

        self.assertEqual(type(result_list), list)
        self.assertEqual(len(result_list), 3)
        self.assertTrue(3 in result_list)
        self.assertTrue(5 in result_list)
        self.assertTrue(42 in result_list)

    def test_deep_find_all_dict_with_nested_lists(self):
        result_list = deep_find_all(self.dict_with_nested_lists, 'apple')

        self.assertEqual(type(result_list), list)
        self.assertEqual(len(result_list), 2)
        self.assertTrue(3 in result_list)
        self.assertTrue(42 in result_list)

    def test_deep_find_all_list_with_dicts(self):
        result_list = deep_find_all(self.list_with_dicts, 'apple')

        self.assertEqual(result_list, [42])

    def test_deep_find_all_with_nothing_found(self):
        with self.subTest('With dict'):
            result_list = deep_find_all({'a': 1, 1: 'a'}, 'apple')

            self.assertEqual(result_list, [])

        with self.subTest('With list'):
            result_list = deep_find_all([{'a': 1, 1: 'a'}, 'Anton'], 'apple')

            self.assertEqual(result_list, [])

    def test_deep_update_with_nested_dicts(self):
        expected = {
            'a': {
                1,
                2
            },
            'b': {
                'apple': 69,
                'd': {
                    'apple': 69
                }
            },
            'apple': 69

        }

        self.assertEqual(
            deep_update(self.nested_dicts, 'apple', 69),
            expected
        )

    def test_deep_update_dict_with_nested_lists(self):
        expected = {'a': [[[{'b': 2}, {'apple': 69}]]], 'apple': 69}

        self.assertEqual(
            deep_update(self.dict_with_nested_lists, 'apple', 69),
            expected
        )

    def test_deep_update_list_with_dicts(self):
        expected = [{}, {'apple': 69}, 'Anton']

        self.assertEqual(
            deep_update(self.list_with_dicts, 'apple', 69),
            expected
        )

    def test_deep_update_updates_nothing(self):
        expected = self.list_with_dicts

        self.assertEqual(
            deep_update(self.list_with_dicts, 'pineapple', 69),
            expected
        )

    def test_deep_apply_with_nested_dicts(self):
        nested_dicts = {
            'b': {
                'apple': 3,
                'd': {
                    'apple': 5
                }
            },
            'apple': 42
        }

        expected = {
            'bX': {
                'appleX': 3,
                'dX': {
                    'appleX': 5
                }
            },
            'appleX': 42
        }

        self.assertEqual(
            deep_apply(lambda x: f'{x}X', nested_dicts),
            expected
        )

    # def test_deep_update_dict_with_nested_lists(self):
    #     expected = {'a': [[[{'b': 2}, {'apple': 69}]]], 'apple': 69}
    #
    #     deep_update(self.dict_with_nested_lists, 'apple', 69)
    #     self.assertEqual(
    #         self.dict_with_nested_lists,
    #         expected
    #     )
    #
    # def test_deep_update_list_with_dicts(self):
    #     expected = [{}, {'apple': 69}, 'Anton']
    #
    #     deep_update(self.list_with_dicts, 'apple', 69)
    #     self.assertEqual(
    #         self.list_with_dicts,
    #         expected
    #     )
    #
    # def test_deep_update_updates_nothing(self):
    #     expected = self.list_with_dicts
    #
    #     deep_update(self.list_with_dicts, 'pineapple', 69)
    #     self.assertEqual(
    #         self.list_with_dicts,
    #         expected
    #     )



if __name__ == '__main__':
    unittest.main()
