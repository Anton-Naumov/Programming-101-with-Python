from models.base_user import BaseUser
from models.vehicle import Vehicle
from models.proxys.client_proxy import ClientProxy
from models.proxys.vehicle_proxy import VehicleProxy
from models.repair_hour import RepairHour
from models.proxys.repair_hour_proxy import RepairHourProxy


class Client(BaseUser):
    def __init__(self, *, id, user_name, email, phone_number, address):
        super().__init__(
            id=id,
            user_name=user_name,
            email=email,
            phone_number=phone_number,
            address=address
        )

    def __str__(self):
        return f'client_name: {self.user_name}, email: {self.email},'\
               f'phone_number: {self.phone_number}, address: {self.address}'

    def get_personal_vehicles(self):
        return [Vehicle.make_vehicle(vrow)
                for vrow in VehicleProxy.get_vehicles_for_client(self.id)]

    def add_vehicle(self, *, category, make, model, register_number, gear_box):
        VehicleProxy.insert_vehicle(
            category=Vehicle.category_validator(category),
            make=Vehicle.make_validator(make),
            model=Vehicle.model_validator(model),
            register_number=Vehicle.register_number_validator(register_number),
            gear_box=Vehicle.gear_box_validator(gear_box),
            owner=self.id
        )

    def get_saved_repair_hours(self):
        return RepairHourProxy.query_repair_hours_for_client(self.id)

    def update_vehicle(self, *, vehicle_id, category, make, model, register_number, gear_box):
        VehicleProxy.update_vehicle(
            Vehicle.category_validator(category),
            Vehicle.make_validator(make),
            Vehicle.model_validator(model),
            Vehicle.register_number_validator(register_number),
            Vehicle.gear_box_validator(gear_box),
            Vehicle.id_validator(vehicle_id)
        )

    def delete_vehicle(self, vehicle_id):
        VehicleProxy.delete_vehicle(Vehicle.id_validator(vehicle_id))

    @classmethod
    def save_repair_hour(cls, *, hour_id, vehicle_id, service_name):
        RepairHourProxy.save_repair_hour(
            hour_id,
            vehicle_id,
            RepairHour.service_name_validator(service_name)
        )

    @classmethod
    def update_repair_hour(cls, *, repair_hour_id, start_hour, bill):
        RepairHourProxy.update_repair_hour_by_id(
            repair_hour_id=repair_hour_id,
            start_hour=RepairHour.hour_validator(start_hour),
            bill=RepairHour.bill_validator(bill)
        )

    @classmethod
    def delete_repair_hour(cls, repair_hour_id):
        RepairHourProxy.delete_repair_hour_by_id(repair_hour_id)

    @classmethod
    def make_client(cls, row):
        return cls(
            id=row[0],
            user_name=row[1],
            email=row[2],
            phone_number=row[3],
            address=row[4]
        )

    @classmethod
    def register_and_get(cls, *, user_name, email, phone_number, address):
        client = cls(
            id=0,
            user_name=user_name,
            email=email,
            phone_number=phone_number,
            address=address
        )
        client.id = ClientProxy.insert_client(
            user_name=user_name,
            email=email,
            phone_number=phone_number,
            address=address
        )
        return client
