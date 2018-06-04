from aggregated_money_tracker import AgregatedMoneyTracker
from category import Expense, Income


class MoneyTracker:
    def __init__(self, file_name=''):
        self._data_base = AgregatedMoneyTracker(file_name)

    def list_user_data(self):
        return str(self._data_base)

    def show_user_data_per_date(self, day, month, year):
        date = f'{year:04d},{month:02d},{day:02d}'
        date_expences = self._data_base.get_expences_for_date(date)
        date_income = self._data_base.get_income_for_date(date)
        return self.get_string(date_income + date_expences)

    @staticmethod
    def get_string(data):
        string = ''
        for x in data:
            string = f'{string}{str(x)}'
        return string

    def get_user_incomes(self):
        incomes = []
        for date in self._data_base.get_sorted_dates():
            incomes.extend(self._data_base.get_income_for_date(date))
        return incomes

    def get_user_expences(self):
        expences = []
        for date in self._data_base.get_sorted_dates():
            expences.extend(self._data_base.get_expences_for_date(date))
        return expences

    def show_user_incomes(self):
        return self.get_string(self.get_user_incomes())

    def show_user_expences(self):
        return self.get_string(self.get_user_expences())

    def list_income_categories(self):
        categories = ''
        for income in self.get_user_incomes():
            categories = f'{categories}{income.get_category()}\n'
        return categories

    def list_expence_categories(self):
        categories = ''
        for expence in self.get_user_expences():
            categories = f'{categories}{expence.get_category()}\n'
        return categories

    def list_user_exepences_ordered_by_categories(self):
        ordered_expences = sorted(self.get_user_expences(),
                                  key=lambda expence: expence.get_category())
        return self.get_string(ordered_expences)

    def add_income(self, day, month, year, category, amount):
        date = f'{year:04d},{month:02d},{day:02d}'
        self._data_base.set_record_for_date(date, Income(category, amount))

    def add_expence(self, day, month, year, category, amount):
        date = f'{year:04d},{month:02d},{day:02d}'
        self._data_base.set_record_for_date(date, Expense(category, amount))
