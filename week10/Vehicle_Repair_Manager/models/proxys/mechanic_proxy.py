from utils import data_base
from settings import DB_NAME
from models.proxys.base_user_proxy import BaseUserProxy
from models.proxys.queries.queries_mechanic import create_mechanic_table,\
                                                   insert_mechanic, query, query_all


class MechanicProxy:
    @classmethod
    @data_base(DB_NAME)
    def create_table(cls, cursor):
        cursor.execute(create_mechanic_table)

    @classmethod
    @data_base(DB_NAME)
    def insert_mechanic(cls, cursor, *, user_name, email, phone_number, address, title):
        id_of_user = BaseUserProxy.insert_user(
            user_name=user_name,
            email=email,
            phone_number=phone_number,
            address=address
        )
        cursor.execute(insert_mechanic, [str(id_of_user), title])
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

    @classmethod
    @data_base(DB_NAME, read_only=True)
    def does_mechanic_exist_by_id(cls, cursor, mechanic_id):
        return cls.query(id=mechanic_id) != []

    @classmethod
    @data_base(DB_NAME, read_only=True)
    def query_all(cls, cursor):
        return cursor.execute(query_all).fetchall()
