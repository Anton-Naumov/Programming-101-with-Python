import hashlib
from models import session
from models import User
from exceptions import InvalidUserInformation


class UserController:
    @classmethod
    def check_id(cls, user_id):
        return session.query(User.id).filter(User.id == user_id).scalar() is not None

    @classmethod
    def login(cls, username, password):
        if session.query(User.id).filter(User.username == username,
                                         User.password == cls.hash_password(password,
                                                                            username)).\
           scalar() is None:
            raise InvalidUserInformation('Wrong user information!')

        return session.query(User).\
            filter(User.username == username,
                   User.password == cls.hash_password(password, username)).one()

    @classmethod
    def register(cls, username, password):
        if username == '':
            raise InvalidUserInformation('The username is not valid!')

        if session.query(User.id).filter(User.username == username).scalar() is not None:
            raise InvalidUserInformation('That username is taken!')

        cls.validate_password(password, username)
        hashed_password = cls.hash_password(password, username)
        session.add(User(username=username, password=hashed_password))
        session.commit()

        return session.query(User).\
            filter(User.username == username, User.password == hashed_password).one()

    @classmethod
    def validate_password(cls, password, username):
        if username in password:
            raise InvalidUserInformation('The password should\'t contain the username!')
        elif len(password) < 8:
            raise InvalidUserInformation('The password should be longer then 8 symbols!')
        elif any(n.isdigit() for n in password) is False:
            raise InvalidUserInformation('The password must contain a digit!')
        elif any(capital.isupper() for capital in password) is False:
            raise InvalidUserInformation('The password must contain a capital letter!')
        elif any(c in '#$%&' for c in password) is False:
            raise InvalidUserInformation('The password must contain a special symbol!')

    @classmethod
    def hash_password(cls, password, username):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode(),
            username.encode(),
            10000
        ).hex()
