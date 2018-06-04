import sys
from utils import catch_and_print_exception
from models.base_user import BaseUser
from models.client import Client
from models.mechanic import Mechanic
from models.exceptions import UserNotRegistered
from models.exceptions import InvalidIndex
from models.exceptions import NotValidUserInformation


class MenuController:
    def __init__(self):
        self.options = {}

    def execute_operation(self, operation):
        if operation in self.options:
            self.options[operation]()
        else:
            self._print('Invalid operation\n')

    @classmethod
    def log_in(cls):
        user_name = cls._read('Hello!\nProvide user name:')

        user = None
        try:
            user = BaseUser.get_user(user_name)
        except UserNotRegistered:
            cls._print('Unknown user!\n')
            user = cls.register()

        return user

    @classmethod
    @catch_and_print_exception(NotValidUserInformation)
    def register(cls):
        decicion = cls._read('Would you like to create new user?\n')

        user = None
        if 'yes' == decicion.lower() or 'y' == decicion.lower():
            decicion = cls._read('Are you a \'client\' or \'mechanic\'?\n')

        if 'client' == decicion:
            user = cls.register_client()
        if 'mechanic' == decicion:
            user = cls.register_mechanic()

        return user

    @classmethod
    def register_client(cls):
        return Client.register_and_get(
            user_name=cls._read('Provide user_name:\n'),
            email=cls._read('Provide email:\n'),
            phone_number=cls._read('Provide phone_number:\n'),
            address=cls._read('Provide address:\n')
        )

    @classmethod
    def register_mechanic(cls):
        return Mechanic.register_and_get(
            user_name=cls._read('Provide user_name:\n'),
            email=cls._read('Provide email:\n'),
            phone_number=cls._read('Provide phone_number:\n'),
            address=cls._read('Provide address:\n'),
            title=cls._read('Provide title:\n')
        )

    @classmethod
    def _print(cls, rows, headers=None):
        from view.vehicle_repair_manager_menu import Vehicle_Repair_Manager_Menu
        from tabulate import tabulate

        if headers is None:
            Vehicle_Repair_Manager_Menu.print_info(rows)
        else:
            Vehicle_Repair_Manager_Menu.print_info(tabulate(
                rows,
                headers=headers,
                tablefmt='orgtbl'
            ))

    @classmethod
    def _read(cls, msg):
        from view.vehicle_repair_manager_menu import Vehicle_Repair_Manager_Menu

        return Vehicle_Repair_Manager_Menu.read_data(msg)

    @classmethod
    def print_hours(cls, hours):
        free_hours = [[pos + 1, row[1], row[2]] for pos, row in enumerate(hours)]
        cls._print(free_hours, ['id', 'Date', 'Hour'])

    @classmethod
    def validate_id(self, id, max):
        if id.isdigit() is False or\
           int(id) < 0 or int(id) > max:
            raise InvalidIndex('The given id is not valid!')

    @classmethod
    def exit(self):
        sys.exit()
