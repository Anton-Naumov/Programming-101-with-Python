import re
import os
from money_tracker import MoneyTracker


class MoneyTrackerMenu:
    def __init__(self):
        os.system('clear')
        self._user_name = input('Enter user name:')
        self.initialize_file_and_money_tracker()
        self.initialize_options()
        self.date_message = '(Format of the date is DD,MM,YYYY)\nEnter date:'

    def initialize_file_and_money_tracker(self):
        information_entered = False
        while information_entered is False:
            try:
                self._file_with_data = input('Enter file to load:')
                self._money_tracker = MoneyTracker(self._file_with_data)
                information_entered = True
                os.system('clear')
            except Exception:
                print('The file name is incorect or its content is invalid!')

    def initialize_options(self):
        self.options = ['1', '2', '3', '4', '5', '6', '7']
        self.options_functions = [self.option_one, self.option_two,
                                  self.option_three, self.option_four,
                                  self.option_five, self.option_six,
                                  self.option_seven]

    def start(self):
        self.working = True
        option_chosen = ''
        while self.working is True:
            self.print_menu_options()
            option_chosen = input()
            if option_chosen not in self.options:
                print('Invalid option, try again!')
            else:
                self.options_functions[int(option_chosen) - 1]()
            if self.working is True:
                input('Press enter to continue:')
            os.system('clear')

    def print_menu_options(self):
        print(f'Hello, {self._user_name}!\n'
              'Choose one of the following options to continue:\n'
              '1 - show all data\n'
              '2 - show data for specific date\n'
              '3 - show expenses, ordered by categories\n'
              '4 - add new income\n'
              '5 - add new expense\n'
              '6 - exit without saving\n'
              '7 - exit and save\n')

    def option_one(self):
        print(self._money_tracker.list_user_data())

    def option_two(self):
        try:
            day, month, year = self.date_parser(input(self.date_message))
            print(self._money_tracker.show_user_data_per_date(day,
                                                              month, year))
        except ValueError as ex:
            print(f'\nError!\n{ex}\n')

    def option_three(self):
        print(self._money_tracker.list_user_exepences_ordered_by_categories())

    def option_four(self):
        try:
            day, month, year = self.date_parser(input(self.date_message))
            category = input('Category of income:')
            amount = self.amount_parser(input('Amount of income:'))
            self._money_tracker.add_income(day, month, year, category, amount)
        except ValueError as ex:
            print(f'\nError!\n{ex}\n')

    def option_five(self):
        try:
            day, month, year = self.date_parser(input(self.date_message))
            category = input('Category of expence:')
            amount = self.amount_parser(input('Amount of expense:'))
            self._money_tracker.add_expence(day, month, year, category, amount)
        except ValueError as ex:
            print(f'\nError!\n{ex}\n')

    def option_six(self):
        self.working = False

    def option_seven(self):
        self.working = False
        self.save_data_in_a_file()

    def save_data_in_a_file(self):
        with open(self._file_with_data, 'w') as f:
            f.write(self._money_tracker.list_user_data())

    @staticmethod
    def date_parser(date):
        if re.match(r'\d{1,2},\d{1,2},\d{4}', date) is None:
            raise ValueError('The date is invalid!')
        parts = date.split(',')
        return int(parts[0]), int(parts[1]), int(parts[2])

    @staticmethod
    def amount_parser(amount):
        try:
            checked_amount = float(amount)
            return checked_amount
        except Exception:
            raise ValueError('The amount should be a number!')
