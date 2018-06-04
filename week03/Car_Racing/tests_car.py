import unittest

from car import Car


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car('AUDI', 'A7', 300)
        self.car1 = Car('NISSAN', 'GTR', 400)

    def test_eq_(self):
        car2 = Car('Toyota', 'A7', 300)
        car3 = Car('AUDI', 'A5', 300)
        car4 = Car('AUDI', 'A7', 250)
        car5 = Car('AUDI', 'A7', 300)
        self.assertNotEqual(self.car, self.car1)
        self.assertNotEqual(self.car, car2)
        self.assertNotEqual(self.car, car3)
        self.assertNotEqual(self.car, car4)
        self.assertEqual(self.car, car5)

    def test_dict_repr(self):
        self.assertEqual(self.car.dict_repr(), {
                                                'car': 'AUDI',
                                                'model': 'A7',
                                                'max_speed': 300
                                               })

    def test_get_car_from_dict(self):
        dict_with_car = {
                         'car': 'AUDI',
                         'model': 'A7',
                         'max_speed': 300
                        }
        self.assertEqual(Car.get_car_from_dict(dict_with_car), self.car)


if __name__ == '__main__':
    unittest.main()
