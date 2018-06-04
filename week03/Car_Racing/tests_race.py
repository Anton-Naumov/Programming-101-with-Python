import unittest

from car import Car
from driver import Driver
from race import Race


class TestCar(unittest.TestCase):
    def setUp(self):
        self.driver1 = Driver('Ivo', Car('Opel', 'Astra', 240))
        self.driver2 = Driver('Rado', Car('Peugeot', '107', 180))
        self.driver3 = Driver('Slavqna', Car('Opel', 'Meriva', 300))
        self.driver4 = Driver('Pavlin', Car('AUDI', 'R8', 380))
        self.driver5 = Driver('Roni', Car('Golf', '5', 200))
        self.driver6 = Driver('Ceco', Car('AUDI', 'Q5', 310))
        self.race = Race([self.driver1, self.driver2, self.driver3,
                          self.driver4, self.driver5, self.driver6], 0.2)

    def test___init___method(self):
        self.assertEqual(self.race._drivers, [self.driver4, self.driver6,
                                              self.driver3, self.driver1,
                                              self.driver5, self.driver2])

    def test_race_with_empty_drivers(self):
        race1 = Race([], 0.2)
        self.assertEqual(race1._drivers, [])
        self.assertEqual(race1._crashed_drivers, [])

    def test_race_with_2_finishers(self):
        self.race._crash_chance = 0.4
        self.race.race()
        self.assertEqual(self.race._drivers,
                         [self.driver1, self.driver5, self.driver2])
        self.assertEqual(self.race._crashed_drivers,
                         [self.driver4, self.driver6, self.driver3])

    def test_results_with_no_drivers(self):
        race1 = Race([], 0.2)
        race1.results()
        self.assertEqual(race1._drivers, [])

    def test_results_add_points(self):
        self.race.results()
        self.assertEqual(self.race._drivers[0].points, 8)
        self.assertEqual(self.race._drivers[1].points, 6)
        self.assertEqual(self.race._drivers[2].points, 4)
        self.assertEqual(self.race._drivers[3].points, 0)

    def test_get_drivers_from_list_no_drivers(self):
        self.assertEqual(Race.get_drivers_from_list({}), [])

    def test_get_drivers_from_list_with_drivers(self):
        drivers_list = [
                          {
                            "name": "Ivo",
                            "car": "Opel",
                            "model": "Astra",
                            "max_speed": 240
                          },
                          {
                            "name": "Rado",
                            "car": "Pegeout",
                            "model": "107",
                            "max_speed": 180
                          }
                      ]
        print(Race.get_drivers_from_list(drivers_list)[0])
        print([self.driver1, self.driver2][0])
        print(Race.get_drivers_from_list(drivers_list)[1])
        print([self.driver1, self.driver2][1])
        self.assertEqual(Race.get_drivers_from_list(drivers_list),
                         [self.driver1, self.driver2])

    def test_update_driver_stats_or_add_update_case(self):
        drivers = [self.driver1, self.driver2, self.driver3,
                   self.driver4, self.driver5]
        updated_driver1 = Driver('Ivo', Car('Opel', 'Astra', 240), 1, 8)
        updated_drivers = Race.update_driver_stats_or_add(drivers,
                                                          updated_driver1)
        self.assertEqual(updated_drivers[0].races_done, 1)
        self.assertEqual(updated_drivers[0].points, 8)


if __name__ == '__main__':
    unittest.main()
