from utils import data_base
from settings import DB_NAME
from models.proxys.base_user_proxy import BaseUserProxy
from models.proxys.queries.queries_client import create_client_table,\
                                                         insert_client_in_table, query


class ClientProxy:
    @classmethod
    @data_base(DB_NAME)
    def create_table(cls, cursor):
        cursor.execute(create_client_table)

    @classmethod
    @data_base(DB_NAME)
    def insert_client(cls, cursor, *, user_name, email, phone_number, address):
        id_of_user = BaseUserProxy.insert_user(
            user_name=user_name,
            email=email,
            phone_number=phone_number,
            address=address
        )
        cursor.execute(insert_client_in_table, [str(id_of_user)])
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
    def does_client_exist_by_id(cls, cursor, client_id):
        return cls.query(id=client_id) != []


if __name__ == '__main__':
    # BaseUserProxy.create_table()
    # ClientProxy.create_table()
    # ClientProxy.insert_client(
    #     user_name='Anton Naumov',
    #     email='antonnaumov1997@gmail.com',
    #     phone_number='0882593780',
    #     address='Sofia, Bulgaria'
    # )
    # ClientProxy.insert_client(
    #     user_name='Vasko Naumov',
    #     email='vasko98@gmail.com',
    #     phone_number='0882593779',
    #     address='Sofia, Bulgaria'
    # )
    # print(ClientProxy.query(id=2, user_name='Anton Naumov'))
    pass
