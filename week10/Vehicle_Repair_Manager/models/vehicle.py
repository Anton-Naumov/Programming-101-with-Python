import re
from models.exceptions import NotValidVehicleData


class Vehicle:
    def __init__(self, *,  id, category, make, model, register_number, gear_box):
        self.id = id
        self.category = category
        self.make = make
        self.model = model
        self.register_number = register_number
        self.gear_box = gear_box

    def __str__(self):
        return f'{self.make} {self.model} with RegNumber: {self.register_number}'

    @classmethod
    def id_validator(cls, id):
        return id

    @classmethod
    def category_validator(cls, category):
        if category == '' or len(category) > 30:
            raise NotValidVehicleData('Invalid category!')
        return category

    @classmethod
    def make_validator(cls, make):
        if make == '' or len(make) > 30:
            raise NotValidVehicleData('Invalid make!')
        return make

    @classmethod
    def model_validator(cls, model):
        if model == '' or len(model) > 30:
            raise NotValidVehicleData('Invalid model!')
        return model

    @classmethod
    def register_number_validator(cls, register_number):
        if re.match('[A-Z] \d{5} [A-Z][A-Z]$', register_number) is None:
            raise NotValidVehicleData('Invalid register number'
                                      'The format is "[A-Z] DDDD [A-Z][A-Z]"!')
        return register_number

    @classmethod
    def gear_box_validator(cls, gear_box):
        if gear_box != 'manual' and gear_box != 'automatic':
            raise NotValidVehicleData('Invalid gear box!')
        return gear_box

    @classmethod
    def make_vehicle(cls, row):
        return cls(
            id=row[0],
            category=row[1],
            make=row[2],
            model=row[3],
            register_number=row[4],
            gear_box=row[5]
        )
