from car import Car


class Driver:
    def __init__(self, name, car, races_done=0, points=0):
        self._name = name
        self._car = car
        self.races_done = races_done
        self.points = points

    def will_crash(self, crash_chance):
        return (self._car._max_speed / 1000 + self.races_done * 0.1
                + crash_chance) > 0.75

    def car_speed(self):
        return self._car._max_speed

    def race(self):
        self.races_done += 1

    def __str__(self):
        return f'Name: {self._name}, car: {self._car}'

    def __eq__(self, other):
        return self._name == other._name and self._car == other._car

    def dict_repr(self):
        driver_dict_repr = self._car.dict_repr()
        driver_dict_repr['name'] = self._name
        driver_dict_repr['races_done'] = self.races_done
        driver_dict_repr['points'] = self.points
        return driver_dict_repr

    @staticmethod
    def get_driver_from_dict(dict_with_driver_info):
        driver = Driver(dict_with_driver_info['name'],
                        Car.get_car_from_dict(dict_with_driver_info))
        if 'races_done' in dict_with_driver_info:
            driver.races_done = dict_with_driver_info['races_done']
        if 'points' in dict_with_driver_info:
            driver.points = dict_with_driver_info['points']
        return driver
