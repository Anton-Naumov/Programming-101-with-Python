import re
from category import Income, Expense


class ParseMoneyTrackerData:
    date_re = re.compile(r'=== \d{1,2}-\d{1,2}-\d{4} ===\n$')
    income_re = re.compile(r'((\d+)|(\d+.\d+)), [ \w]+, New Income\n$')
    expence_re = re.compile(r'((\d+)|(\d+.\d+)), [ \w]+, New Expense\n$')

    @classmethod
    def parse_row(cls, row):
        parsed_row = cls.parse_date(row)
        if parsed_row is not None:
            return parsed_row
        parsed_row = cls.parse_income(row)
        if parsed_row is not None:
            return parsed_row
        parsed_row = cls.parse_expence(row)
        if parsed_row is not None:
            return parsed_row
        raise ValueError('The row doesn`t match the any re!')

    @classmethod
    def parse_date(cls, row):
        checked_row = cls.date_re.match(row)
        if checked_row is None:
            return None
        parts = re.findall('\d+', checked_row.group())
        return f'{parts[2]},{parts[1]},{parts[0]}'

    @classmethod
    def parse_expence(cls, row):
        checked_row = cls.expence_re.match(row)
        if checked_row is None:
            return None
        parts = checked_row.group().split(', ')
        return Expense(parts[1], float(parts[0]))

    @classmethod
    def parse_income(cls, row):
        checked_row = cls.income_re.match(row)
        if checked_row is None:
            return None
        parts = checked_row.group().split(', ')
        return Income(parts[1], float(parts[0]))

    @classmethod
    def parse_lines(cls, lines):
        dates_dict = {}
        date = ''
        for line in lines:
            record = cls.parse_row(line)
            dates_dict, date = cls.add_record(dates_dict, date, record)
        return dates_dict

    @classmethod
    def add_record(cls, dates_dict, date, record):
        if type(record) is str:  # That means that it is date
            return dates_dict, record
        dates_dict[date] = dates_dict.get(date, {'income': [],
                                                 'expence': []})
        if type(record) is Income:
            dates_dict[date]['income'].append(record)
        if type(record) is Expense:
            dates_dict[date]['expence'].append(record)
        return dates_dict, date
