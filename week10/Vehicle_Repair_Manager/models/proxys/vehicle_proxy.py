from utils import data_base
from settings import DB_NAME
from models.proxys.queries.queries_vehicle import create_vehicle_table, insert_vehicle,\
                                        delete_vehicle, get_vehicles_for_client,\
                                        update_vehicle, query_vehicle


class VehicleProxy:
    @classmethod
    @data_base(DB_NAME)
    def create_table(cls, cursor):
        cursor.execute(create_vehicle_table)

    @classmethod
    @data_base(DB_NAME)
    def insert_vehicle(cls, cursor, *, category, make, model, register_number, gear_box, owner):
        cursor.execute(insert_vehicle, {
            'category': category,
            'make': make,
            'model': model,
            'register_number': register_number,
            'gear_box': gear_box,
            'owner': owner
        })
        return cursor.lastrowid

    @classmethod
    @data_base(DB_NAME)
    def delete_vehicle(cls, cursor, id):
        cursor.execute(delete_vehicle, str(id))

    @classmethod
    @data_base(DB_NAME, read_only=True)
    def get_vehicles_for_client(cls, cursor, client_id):
        return cursor.execute(get_vehicles_for_client, [str(client_id)]).fetchall()

    @classmethod
    @data_base(DB_NAME)
    def update_vehicle(cls, cursor, category, make, model, register_number, gear_box, id):
        cursor.execute(update_vehicle, {
            'category': category,
            'make': make,
            'model': model,
            'register_number': register_number,
            'gear_box': gear_box,
            'id': id
        })

    @classmethod
    @data_base(DB_NAME, read_only=True)
    def query(cls, cursor, client_id):
        return cursor.execute(query_vehicle, str(client_id)).fetchall()

    @classmethod
    @data_base(DB_NAME, read_only=True)
    def does_vehicle_exist_by_id(cls, cursor, client_id):
        return cls.query(client_id) != []


if __name__ == '__main__':
    # VehicleProxy.create_table()
    # VehicleProxy.insert_vehicle(
    #     category='sedan',
    #     make='AUDI',
    #     model='A7',
    #     register_number='12345',
    #     gear_box='manual',
    #     owner=1
    # )
    # VehicleProxy.insert_vehicle(
    #     category='sedan',
    #     make='AUDI',
    #     model='A5',
    #     register_number='12346',
    #     gear_box='manual',
    #     owner=2
    # )
    # VehicleProxy.delete_vehicle(3)
    # print(VehicleProxy.get_vehicles_for_client(2))
    # VehicleProxy.update_vehicle(
    #     category='sedan',
    #     make='AUDI',
    #     model='Q7',
    #     register_number='12346',
    #     gear_box='automatic',
    #     id=2
    # )
    pass
