from utils import data_base
from settings import DB_NAME
from models.proxys.mechanic_proxy import MechanicProxy
from models.proxys.vehicle_proxy import VehicleProxy
from models.proxys.mechanic_service_proxy import MechanicServiceProxy
from models.proxys.queries.queries_repair_hour import create_repair_hour_table,\
                insert_repair_hour, list_all_free_hours, list_all_free_hours_for_date,\
                list_all_busy_hours, list_all_busy_hours_for_date,\
                save_repair_hour, delete_repair_hour,\
                query_repair_hour, update_repair_hour_by_id,\
                list_repair_hours_for_client,\
                list_all_free_hours_for_mechanic, list_all_free_hours_for_mechanic_for_date


class RepairHourProxy:
    @classmethod
    @data_base(DB_NAME)
    def create_table(cls, cursor):
        cursor.execute(create_repair_hour_table)

    @classmethod
    @data_base(DB_NAME)
    def add_new_repair_hour(cls, cursor, *, date, start_hour, bill, mechanic_id):
        if MechanicProxy.does_mechanic_exist_by_id(mechanic_id) is False:
            raise Exception('Invalid mechanic id!')

        id_of_mechanic_service = MechanicServiceProxy.insert_mechanic_service(mechanic_id)

        cursor.execute(insert_repair_hour, {
            'date': date,
            'start_hour': start_hour,
            'bill': bill,
            'mechanic_service': id_of_mechanic_service
        })

    @classmethod
    @data_base(DB_NAME)
    def list_all_free_hours(cls, cursor):
        return cursor.execute(list_all_free_hours).fetchall()

    @classmethod
    @data_base(DB_NAME)
    def list_all_free_hours_for_date(cls, cursor, date):
        return cursor.execute(list_all_free_hours_for_date, [date]).fetchall()

    @classmethod
    @data_base(DB_NAME)
    def list_all_busy_hours(cls, cursor, mechanic_id):
        return cursor.execute(list_all_busy_hours, [mechanic_id]).fetchall()

    @classmethod
    @data_base(DB_NAME)
    def list_all_free_hours_for_mechanic(cls, cursor, mechanic_id):
        return cursor.execute(list_all_free_hours_for_mechanic, [mechanic_id]).fetchall()

    @classmethod
    @data_base(DB_NAME)
    def list_all_free_hours_for_mechanic_for_date(cls, cursor, date, mechanic_id):
        return cursor.execute(list_all_free_hours_for_mechanic_for_date,
                              [date, mechanic_id]).fetchall()

    @classmethod
    @data_base(DB_NAME)
    def list_all_busy_hours_for_date(cls, cursor, date, mechanic_id):
        return cursor.execute(list_all_busy_hours_for_date, [date, mechanic_id]).fetchall()

    @classmethod
    @data_base(DB_NAME, read_only=True)
    def query(cls, cursor, repair_hour_id):
        return cursor.execute(query_repair_hour, [repair_hour_id]).fetchall()

    @classmethod
    @data_base(DB_NAME, read_only=True)
    def does_repair_hour_exist_by_id(cls, cursor, repair_hour_id):
        return cls.query(repair_hour_id) != []

    @classmethod
    @data_base(DB_NAME, read_only=True)
    def query_repair_hours_for_client(cls, cursor, client_id):
        return cursor.execute(list_repair_hours_for_client, [str(client_id)]).fetchall()

    @classmethod
    @data_base(DB_NAME, db_parameter=True)
    def save_repair_hour(cls, db, cursor, hour_id, vehicle_id, service_name):
        if VehicleProxy.does_vehicle_exist_by_id(vehicle_id) is False:
            raise Exception('Vehicle id "{}" doesn\'t exist!'.format(vehicle_id))

        if cls.does_repair_hour_exist_by_id(hour_id) is False:
            raise Exception('Repair hour id "{}" doesn\'t exist!'.format(hour_id))

        cursor.execute(save_repair_hour, [vehicle_id, hour_id])

        db.commit()

        mechanic_service_id = cls.query(hour_id)[0][5]
        MechanicServiceProxy.add_service_to_mechanic_service(mechanic_service_id, service_name)

    @classmethod
    @data_base(DB_NAME)
    def delete_repair_hour_by_id(cls, cursor, repair_hour_id):
        if cls.does_repair_hour_exist_by_id(repair_hour_id) is True:
            cursor.execute(delete_repair_hour, [repair_hour_id])

    @classmethod
    @data_base(DB_NAME)
    def update_repair_hour_by_id(cls, cursor, *, repair_hour_id, start_hour, bill):
        if cls.does_repair_hour_exist_by_id(repair_hour_id) is False:
            raise Exception('Repair hour id "{}" doesn\'t exist!'.format(repair_hour_id))
        cursor.execute(update_repair_hour_by_id, {
            'start_hour': start_hour,
            'bill': bill,
            'id': repair_hour_id
        })


if __name__ == '__main__':
    # MechanicServiceProxy.create_mechanic_service_table()
    # RepairHourProxy.create_table()
    # RepairHourProxy.add_new_repair_hour(
    #     date='12-05-2018',
    #     start_hour='10:15',
    #     bill='25',
    #     mechanic_id=4
    # )
    # RepairHourProxy.add_new_repair_hour(
    #     date='15-15-2018',
    #     start_hour='12:15',
    #     bill='35',
    #     mechanic_id=5
    # )
    # RepairHourProxy.save_repair_hour(2, 2, 'Oil Change')
    # RepairHourProxy.add_new_repair_hour(
    #     date='05-10-2018',
    #     start_hour='10:15',
    #     bill='35',
    #     mechanic_id=5
    # )
    # print(RepairHourProxy.list_all_free_hours())
    # print(RepairHourProxy.list_all_busy_hours())
    # print(RepairHourProxy.list_all_free_hours_for_date('12-05-2018'))
    # print(RepairHourProxy.list_all_busy_hours_for_date('12-05-2018'))
    # RepairHourProxy.delete_repair_hour_by_id(2)
    # RepairHourProxy.update_repair_hour_by_id(
    #     repair_hour_id=8,
    #     start_hour='10:45',
    #     bill='50'
    # )
    pass
