from utils import data_base
from settings import DB_NAME
from models.proxys.mechanic_proxy import MechanicProxy
from models.proxys.queries.queries_mechanic_service import create_mechanic_service_table,\
                                   insert_mechanic_service, insert_service, query_service,\
                                   update_service_to_mechanic, query_all_services,\
                                   remove_service_from_mechanic_service,\
                                   create_service_table


class MechanicServiceProxy:
    @classmethod
    @data_base(DB_NAME)
    def create_mechanic_service_table(cls, cursor):
        cursor.execute(create_mechanic_service_table)

    @classmethod
    @data_base(DB_NAME)
    def create_service_table(cls, cursor):
        cursor.execute(create_service_table)

    @classmethod
    @data_base(DB_NAME)
    def insert_service(cls, cursor, service_name):
        if cursor.execute(query_service, [service_name]).fetchall() == []:
            cursor.execute(insert_service, [service_name])

    @classmethod
    @data_base(DB_NAME)
    def insert_mechanic_service(cls, cursor, mechanic_id, service_id=None):
        if MechanicProxy.does_mechanic_exist_by_id(mechanic_id) is False:
            raise Exception('Invalid mechanic id!')

        cursor.execute(insert_mechanic_service, {
            'mechanic_id': mechanic_id,
            'service_id': service_id
        })
        return cursor.lastrowid

    @classmethod
    @data_base(DB_NAME)
    def add_service_to_mechanic_service(cls, cursor, mechanic_service_id, service_name):
        service = cursor.execute(query_service, [service_name]).fetchall()
        if service == []:
            raise Exception('Service with name "{}" doesn\'t exist!'.format(service_name))

        cursor.execute(update_service_to_mechanic, [service[0][0], mechanic_service_id])

    @classmethod
    @data_base(DB_NAME)
    def remove_service_from_mechanic_service(cls, cursor, mechanic_service_id):
        cursor.execute(remove_service_from_mechanic_service, str(mechanic_service_id))

    @classmethod
    @data_base(DB_NAME, read_only=True)
    def query_all_services(cls, cursor):
        return [service[0] for service in cursor.execute(query_all_services).fetchall()]


if __name__ == '__main__':
    # MechanicServiceProxy.create_mechanic_service_table()
    # MechanicServiceProxy.create_service_table()
    # print(MechanicServiceProxy.insert_mechanic_service(4))
    # MechanicServiceProxy.add_service_to_mechanic_service(1, 'Tire Change')
    # print(MechanicServiceProxy.query_all_services())
    pass
