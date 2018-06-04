import re
from parse_money_tracker_data import ParseMoneyTrackerData
from category import Expense, Income


class AgregatedMoneyTracker:
    def __init__(self, file_name=''):
        if file_name == '':
            self._data = {}
            return
        with open(file_name, 'r') as f:
            lines = f.readlines()
        self._data = ParseMoneyTrackerData.parse_lines(lines)

    def __str__(self):
        result = ''
        for date in self.get_sorted_dates():
            result = f'{result}{self.get_date_str(date)}'
            for record in self._data[date]['income']:
                result = f'{result}{str(record)}'
            for record in self._data[date]['expence']:
                result = f'{result}{str(record)}'
        return result

    def get_sorted_dates(self):
        return sorted(self._data.keys())

    def set_record_for_date(self, date, new_record):
        parsed_new_record = new_record
        if type(new_record) is not Expense and type(new_record) is not Income:
            parsed_new_record = ParseMoneyTrackerData.parse_row(new_record)
        if re.match('\d{4},\d{1,2},\d{1,2}$', date) is None:
            raise ValueError('The date is invalid!')
        self._data, _ = ParseMoneyTrackerData.add_record(self._data,
                                                         date,
                                                         parsed_new_record)

    def get_expences_for_date(self, date):
        if date not in self._data:
            return []
        return self._data[date]['expence']

    def get_income_for_date(self, date):
        if date not in self._data:
            return []
        return self._data[date]['income']

    @staticmethod
    def get_date_str(data):
        date_re = re.compile('\d{4},\d{1,2},\d{1,2}$')
        data_matched = date_re.match(data)
        if data_matched is None:
            raise ValueError('The date doesn`t match the format')
        data_split = data_matched.group().split(',')
        return f'=== {data_split[2]}-{data_split[1]}-{data_split[0]} ===\n'
