class Category:
    def __init__(self, category):
        self._category = category

    def __str__(self):
        return self._category

    def __eq__(self, other):
        return self._category == other._category

    def get_category(self):
        return self._category


class Expense(Category):
    def __init__(self, category, amount):
        super().__init__(category)
        self._amount = amount

    def __str__(self):
        return f'{self._amount:g}, {super().__str__()}, New Expense\n'

    def __eq__(self, other):
        return (super().__eq__(other) and self._amount == other._amount)

    def get_amount(self):
        return self._amount


class Income(Category):
    def __init__(self, category, amount):
        super().__init__(category)
        self._amount = amount

    def __str__(self):
        return f'{self._amount:g}, {super().__str__()}, New Income\n'

    def __eq__(self, other):
        return (super().__eq__(other) and self._amount == other._amount)

    def get_amount(self):
        return self._amount
