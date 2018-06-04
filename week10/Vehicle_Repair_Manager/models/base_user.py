import re
from models.exceptions import UserNotRegistered
from models.exceptions import NotValidUserInformation
from models.proxys.base_user_proxy import BaseUserProxy
from models.proxys.client_proxy import ClientProxy
from models.proxys.mechanic_proxy import MechanicProxy


class BaseUser:
    def __init__(self, *, id, user_name, email, phone_number, address):
        self.id = self.id_validator(id)
        self.user_name = self.user_name_validator(user_name)
        self.email = self.email_validator(email)
        self.phone_number = self.phone_number_validator(phone_number)
        self.address = self.address_validator(address)

    def __str__(self):
        return f'user_name: {self.user_name}, email: {self.email},'\
               f'phone_number: {self.phone_number}, address: {self.address}'

    def __repr__(self):
        return str(self)

    @classmethod
    def id_validator(cls, id):
        return id

    @classmethod
    def user_name_validator(cls, user_name):
        if type(user_name) is not str or len(user_name) > 30 or '\n' in user_name:
            raise NotValidUserInformation('Invalid user name!')
        return user_name

    @classmethod
    def email_validator(cls, email):
        if len(email) > 50 or not re.match('[a-zA-Z0-9]+@[a-zA-Z0-9]+.com$', email):
            raise NotValidUserInformation('Invalid email!')
        return email

    @classmethod
    def phone_number_validator(cls, phone_number):
        if len(phone_number) != 10 or not phone_number.isdigit():
            raise NotValidUserInformation('Invalid phone_number!'
                                          'Phone number should have 10 digits!')
        return phone_number

    @classmethod
    def address_validator(cls, address):
        if len(address) > 30:
            raise NotValidUserInformation('Invalid address!')
        return address

    @classmethod
    def is_user_registered(cls, name):
        result = BaseUserProxy.query(user_name=name)
        if result == []:
            return False
        else:
            return result[0][0]  # there is only one user because the user_name is qnique

    @classmethod
    def get_user(cls, name):
        user_id = cls.is_user_registered(name)

        if user_id is False:
            raise UserNotRegistered()

        user = ClientProxy.query(id=user_id)
        if user != []:
            from models.client import Client
            return Client.make_client(user[0])

        user = MechanicProxy.query(id=user_id)
        if user != []:
            from models.mechanic import Mechanic
            return Mechanic.make_mechanic(user[0])

        raise Exception('Why are you here!')
