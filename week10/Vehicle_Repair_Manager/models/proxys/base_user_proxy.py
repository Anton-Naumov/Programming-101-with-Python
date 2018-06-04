import sqlite3
from utils import data_base
from settings import DB_NAME
from models.proxys.queries.queries_base_user import create_base_user_table,\
                                                    insert_in_base_user, query


class BaseUserProxy:
    @classmethod
    @data_base(DB_NAME)
    def create_table(cls, cursor):
        cursor.execute(create_base_user_table)

    @classmethod
    @data_base(DB_NAME)
    def insert_user(cls, cursor, *, user_name, email, phone_number, address):
        from models.exceptions import NotValidUserInformation
        try:
            cursor.execute(insert_in_base_user, {
                'user_name': user_name,
                'email': email,
                'phone_number': phone_number,
                'address': address
            })
        except sqlite3.IntegrityError:
            raise NotValidUserInformation('This user has already been registered!')
        return cursor.lastrowid

    @classmethod
    @data_base(DB_NAME, read_only=True)
    def query(cls, cursor, *, id=None, user_name=None, email=None, phone_number=None):
        return cursor.execute(query, [
            id,
            user_name,
            email,
            phone_number
        ]).fetchall()


if __name__ == '__main__':
    BaseUserProxy.create_table()
    print(BaseUserProxy.query(id=1))
