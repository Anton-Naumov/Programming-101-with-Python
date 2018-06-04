import serializers


class AttrClass(serializers.JsonableMixin):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Car(serializers.JsonableMixin):
    def __init__(self, *, car, model, year):
        self.car = car
        self.model = model
        self.year = year

    def __eq__(self, other):
        return (
            self.car == other.car,
            self.model == other.model,
            self.year == other.year
        )


class Pet:
    def __init__(self):
        self.name = 'Jonny'
