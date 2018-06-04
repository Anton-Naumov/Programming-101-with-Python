import unittest
from test_classes import AttrClass, Car, Pet


class TestsJsonableMixin(unittest.TestCase):
    def setUp(self):
        self.primitive_attr = AttrClass(
            age=20,
            height=190.5,
            name='Anton',
            is_student=True,
            interests=['coding', 'sleeping'],
            skills={'C++': 100, 'Java': 150},
            job=None
        )

        self.non_primitive_attr = AttrClass(
            name='Anton',
            car=Car(car='AUDI', model='A7', year=2018)
        )

        self.car = Car(car='AUDI', model='A7', year=2018)

    def test_get_serializable_dict_working_correctly(self):
        with self.subTest('With primitive class attrs'):
            expected = {
                "class_name": 'AttrClass',
                "dict": {
                        'age': 20,
                        'height': 190.5,
                        'name': 'Anton',
                        'is_student': True,
                        'interests': ['coding', 'sleeping'],
                        'skills': {'C++': 100, 'Java': 150},
                        'job': None
                }
            }

            self.assertDictEqual(
                expected,
                self.primitive_attr.get_serializable_dict()
            )

        with self.subTest('With non primitive attrs that are JsonableMixin'):
            expected = {
                "class_name": 'AttrClass',
                "dict": {
                    'name': 'Anton',
                    'car': {
                        "class_name": "Car",
                        "dict": {
                            'car': 'AUDI',
                            'model': 'A7',
                            'year': 2018
                        }
                    }
                }
            }

            self.assertDictEqual(
                expected,
                self.non_primitive_attr.get_serializable_dict()
            )

    def test_get_serializable_dict_throwing_exception(self):
        with self.subTest('When the class has attr that is not JsonableMixin'):
            with_non_json_attr = AttrClass(pet=Pet())

            with self.assertRaises(ValueError) as e:
                with_non_json_attr.get_serializable_dict()

            self.assertEqual(
                'The class has non serializable attribute!',
                str(e.exception)
            )

    def test_to_json_working_correctly(self):
        example_inst = AttrClass(
            name='Anton',
            car=self.car
        )

        expected = ('{\n'
                    '    "class_name": "AttrClass",\n'
                    '    "dict": {\n'
                    '        "name": "Anton",\n'
                    '        "car": {\n'
                    '            "class_name": "Car",\n'
                    '            "dict": {\n'
                    '                "car": "AUDI",\n'
                    '                "model": "A7",\n'
                    '                "year": 2018\n'
                    '            }\n'
                    '        }\n'
                    '    }\n'
                    '}')

        self.assertEqual(expected, example_inst.to_json(indent=4))

    def test_from_json_throwing_exception(self):
        with self.subTest('The "class_name" in json_string dict is different'
                          'than the class that called from_json method'):
            with self.assertRaises(Exception) as e:
                AttrClass.from_json(self.car.to_json(indent=4))
            self.assertEqual(
                'The serialized class is not correct!',
                str(e.exception)
            )

    def tests_from_json_working_correctly(self):
        with self.subTest('With primitive types only'):
            json_string = ('{\n'
                           '    "class_name": "AttrClass",\n'
                           '    "dict": {\n'
                           '        "name": "Anton",\n'
                           '        "age": 20,\n'
                           '        "skills": {\n'
                           '            "C++": 100\n'
                           '        }\n'
                           '    }\n'
                           '}')

            extracted_inst = AttrClass.from_json(json_string)

            expected = AttrClass(name='Anton', age=20, skills={'C++': 100})

            self.assertEqual(expected, extracted_inst)

        with self.subTest('With non primitive types'):
            json_string = ('{\n'
                           '    "class_name": "AttrClass",\n'
                           '    "dict": {\n'
                           '        "name": "Anton",\n'
                           '        "car": {\n'
                           '            "class_name": "Car",\n'
                           '            "dict": {\n'
                           '                "car": "AUDI",\n'
                           '                "model": "A7",\n'
                           '                "year": 2018\n'
                           '            }\n'
                           '        }\n'
                           '    }\n'
                           '}')

            result = AttrClass.from_json(json_string)

            self.assertEqual(result, self.non_primitive_attr)


if __name__ == '__main__':
    unittest.main()
