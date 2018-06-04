from exceptions import InvalidPassword


class Client():
    def __init__(self, id, username, balance, message, email):
        self.__id = id
        self.__username = username
        self.__balance = balance
        self.__message = message
        self.__email = email

    def get_username(self):
        return self.__username

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        self.__balance = new_balance

    def get_id(self):
        return self.__id

    def get_message(self):
        return self.__message

    def set_message(self, new_message):
        self.__message = new_message

    @classmethod
    def validate_password(cls, password, username):
        if username in password:
            raise InvalidPassword('The password should\'t contain the username!')
        elif len(password) < 8:
            raise InvalidPassword('The password should be longer then 8 symbols!')
        elif any(n.isdigit() for n in password) is False:
            raise InvalidPassword('The password must contain a digit!')
        elif any(capital.isupper() for capital in password) is False:
            raise InvalidPassword('The password must contain a capital letter!')
        elif any(c in '#$%&' for c in password) is False:
            raise InvalidPassword('The password must contain a special symbol!')
