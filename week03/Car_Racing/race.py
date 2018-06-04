import json
from driver import Driver


class Race:
    def __init__(self, drivers, crash_chance):
        self._drivers = sorted(drivers, key=lambda driver: driver.car_speed(),
                               reverse=True)
        self._crash_chance = crash_chance
        self._crashed_drivers = []

    def race(self):
        finished_drivers = []
        crashed_drivers = []
        for driver in self._drivers:
            driver.race()
            if driver.will_crash(self._crash_chance):
                crashed_drivers.append(driver)
            else:
                finished_drivers.append(driver)
        self._drivers, self._crashed_drivers = (finished_drivers,
                                                crashed_drivers)

    def results(self):
        self.race()
        for x in [0, 2, 4]:
            if x // 2 < len(self._drivers):
                self._drivers[x // 2].points += 8 - x

    @staticmethod
    def get_drivers_from_list(dict_with_drivers):
        drivers = []
        for driver in dict_with_drivers:
            drivers.append(Driver.get_driver_from_dict(driver))
        return drivers

    @staticmethod
    def get_drivers_from_file(file_name):
        with open(file_name, 'r') as f:
            drivers_from_file = json.load(f)
        return Race.get_drivers_from_list(drivers_from_file['people'])

    @staticmethod
    def update_driver_stats_or_add(drivers, update_driver):
        if update_driver in drivers:
            idx = drivers.index(update_driver)
            drivers[idx].races_done = update_driver.races_done
            drivers[idx].points = update_driver.points
        else:
            drivers.append(update_driver)
        return drivers

    @staticmethod
    def make_standings(old_drivers, updated_drivers):
        for driver in updated_drivers:
            old_drivers = Race.update_driver_stats_or_add(old_drivers, driver)
        return sorted(old_drivers, key=lambda driver: driver.points,
                      reverse=True)

    def update_results_file(self):
        pass


if __name__ == '__main__':
    print(Race.get_drivers_from_file('cars.json'))
