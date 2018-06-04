import unittest

from driver import Driver
from car import Car


class TestCar(unittest.TestCase):
    def setUp(self):
        self.driver = Driver('Anton', Car('AUDI', 'A7', 300), 0, 0)
        self.driver1 = Driver('Vasko', Car('NISSAN', 'GTR', 400), 0, 0)

    def test_will_crash(self):
        self.assertEqual(self.driver.will_crash(0.3), False)
        self.assertEqual(self.driver.will_crash(0.46), True)

    def test_eq_(self):
        self.assertEqual(self.driver.__eq__(self.driver1), False)
        self.driver2 = Driver('Anton', Car('AUDI', 'A7', 300), 2, 16)
        self.assertEqual(self.driver.__eq__(self.driver2), True)

    def test_dict_repr(self):
        self.assertEqual(self.driver.dict_repr(),
                         {
                            'name': 'Anton',
                            'car': 'AUDI',
                            'model': 'A7',
                            'max_speed': 300,
                            'races_done': 0,
                            'points': 0
                         })

    def test_driver_from_dict_with_no_races_done_and_points(self):
        dict_with_driver = {
                               'name': 'Anton',
                               'car': 'AUDI',
                               'model': 'A7',
                               'max_speed': 300
                            }
        driver = Driver.get_driver_from_dict(dict_with_driver)
        self.assertEqual(driver, Driver('Anton', Car('AUDI', 'A7', 300)))
        self.assertEqual(driver.races_done, 0)
        self.assertEqual(driver.points, 0)

    def test_driver_from_dict_with_races_done_and_points(self):
        dict_with_driver = {
                               'name': 'Anton',
                               'car': 'AUDI',
                               'model': 'A7',
                               'max_speed': 30,
                               'races_done': 2,
                               'points': 16
                            }
        driver = Driver.get_driver_from_dict(dict_with_driver)
        self.assertEqual(driver.races_done, 2)
        self.assertEqual(driver.points, 16)


if __name__ == '__main__':
    unittest.main()
