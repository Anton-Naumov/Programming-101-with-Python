class Car:
    def __init__(self, car, model, max_speed):
        self._car = car
        self._model = model
        self._max_speed = max_speed

    def __str__(self):
        return (f'Car - {self._car}, model: - '
                f'{self._model}, max_speed - {self._max_speed}')

    def __eq__(self, other):
        return (self._car == other._car and self._model == other._model and
                self._max_speed == other._max_speed)

    def dict_repr(self):
        return {
            'car': self._car,
            'model': self._model,
            'max_speed': self._max_speed,
        }

    @staticmethod
    def get_car_from_dict(dict_with_car_info):
        return Car(dict_with_car_info['car'], dict_with_car_info['model'],
                   dict_with_car_info['max_speed'])
