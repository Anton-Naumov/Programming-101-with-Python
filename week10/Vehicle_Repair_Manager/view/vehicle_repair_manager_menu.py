import sys
from models.client import Client
from models.mechanic import Mechanic
from controllers.menu_controller import MenuController
from controllers.client_controller import ClientController
from controllers.mechanic_controller import MechanicController


class Vehicle_Repair_Manager_Menu:
    @classmethod
    def read_data(cls, msg):
        return input(msg)

    @classmethod
    def print_info(cls, info):
        print(info)

    def __init__(self):
        self.user = MenuController.log_in()
        if self.user is None:
            sys.exit()

        if isinstance(self.user, Client):
            self.menu_controller = ClientController(self.user)
        elif isinstance(self.user, Mechanic):
            self.menu_controller = MechanicController(self.user)
        else:
            raise Exception('What!!!')

    def start(self):
        operation = ''
        while operation != 'exit':
            print(self.menu_controller.MENU)
            operation = input('command> :')
            self.menu_controller.execute_operation(operation)
