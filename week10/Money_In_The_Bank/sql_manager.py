import hashlib
import psycopg2
import time
import datetime
import smtplib
from email.mime.text import MIMEText
from utils import add_one_entry_to_datetime_string, DATETIME_FORMAT
from client import Client
from exceptions import UsernameTaken, UserNotRegistered
from queries import create_query, update_message, insert_sql, select_query,\
                    select_query_by_name_and_password, drop_query,\
                    change_password, select_query_by_name,\
                    get_password_by_username, change_balance_by_id


class SQLManager:
    @classmethod
    def initialize_database(cls, *, dbname, user):
        cls.conn = psycopg2.connect(f"dbname={dbname} user={user}")
        cls.cursor = cls.conn.cursor()

    @classmethod
    def close_database(cls):
        cls.cursor.close()
        cls.conn.close()

    @classmethod
    def create_clients_table(cls):
        cls.cursor.execute(create_query)

    @classmethod
    def drop_clients_table(cls):
        cls.cursor.execute(drop_query)

    @classmethod
    def change_message(cls, new_message, logged_user):
        cls.cursor.execute(update_message, [new_message, logged_user.get_id()])
        cls.conn.commit()
        logged_user.set_message(new_message)

    @classmethod
    def change_pass(cls, new_pass, logged_user):
        Client.validate_password(new_pass, logged_user.get_username())

        new_pass = cls.hash_password(new_pass, logged_user.get_username())

        cls.cursor.execute(change_password, [new_pass, logged_user.get_id()])
        cls.conn.commit()

    @classmethod
    def register(cls, username, password, email):
        Client.validate_password(password, username)

        hash = cls.hash_password(password, username)
        try:
            cls.cursor.execute(insert_sql, (username, str(hash), email))
            cls.conn.commit()
        except psycopg2.IntegrityError:
            raise UsernameTaken('The given username was already taken!')

    @classmethod
    def hash_password(cls, password, username):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode(),
            username.encode(),
            10000
        ).hex()

    @classmethod
    def add_one_entry_to_user_message(cls, user):
        msg = user.get_message()
        currdt = datetime.datetime.now()

        if msg is '' or msg is None:
            cls.change_message(f'{currdt.strftime(DATETIME_FORMAT)}#1', user)
        else:
            cls.change_message(
                add_one_entry_to_datetime_string(msg, currdt),
                user
            )

    @classmethod
    def deposit_money(cls, deposit, user):
        if deposit.isdigit() is False:
            raise Exception('Invalid deposit!')

        cls.cursor.execute(change_balance_by_id, [user.get_balance() + float(deposit),
                                                  user.get_id()])

        user.set_balance(user.get_balance() + float(deposit))

    @classmethod
    def withdraw_money(cls, money, user):
        if money.isdigit() is False:
            raise Exception('Withdraw error!')

        if float(money) < user.get_balance():
            raise Exception('Not enough money to withdraw!')

        cls.cursor.execute(change_balance_by_id, [user.get_balance() - float(money),
                                                  user.get_id()])

        user.set_balance(user.get_balance() - float(money))

    @classmethod
    def send_email_to_user(cls, username):
        cls.cursor.execute(get_password_by_username, [username])
        user_pass = cls.cursor.fetchone()

        if user_pass is None:
            raise UserNotRegistered('There is no user with name "{}"!'.format(username))

        # add email sending

    @classmethod
    def login(cls, username, password):
        hash_password = cls.hash_password(password, username)
        cls.cursor.execute(select_query_by_name_and_password, [username, hash_password])
        user = cls.cursor.fetchone()
        if user:
            logged_user = Client(user[0], user[1], user[2], user[3], user[4])
            cls.change_message('', logged_user)
            return logged_user
        else:
            cls.cursor.execute(select_query_by_name, [username])
            user_by_name = cls.cursor.fetchone()

            if user_by_name:
                cls.add_one_entry_to_user_message(Client(user_by_name[0], user_by_name[1],
                                                         user_by_name[2], user_by_name[3],
                                                         user_by_name[4]))

            return False
