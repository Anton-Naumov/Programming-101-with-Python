from models.repair_hour import RepairHour
from models.base_user import BaseUser
from models.proxys.mechanic_proxy import MechanicProxy
from models.proxys.repair_hour_proxy import RepairHourProxy
from models.proxys.mechanic_service_proxy import MechanicServiceProxy


class Mechanic(BaseUser):
    def __init__(self, *, id, user_name, email, phone_number, address, title):
        super().__init__(
            id=id,
            user_name=user_name,
            email=email,
            phone_number=phone_number,
            address=address
        )
        self.title = title

    def __str__(self):
        return f'client_name: {self.user_name}, email: {self.email},'\
               f'phone_number: {self.phone_number}, address: {self.address},'\
               f'title: {self.title}'

    def add_new_repair_hour(self, *, date, start_hour, bill):
        RepairHourProxy.add_new_repair_hour(
            date=RepairHour.date_validator(date),
            start_hour=RepairHour.hour_validator(start_hour),
            bill=RepairHour.bill_validator(bill),
            mechanic_id=self.id
        )

    @classmethod
    def update_repair_hour(self, *, repair_hour_id, start_hour, bill):
        RepairHourProxy.update_repair_hour_by_id(
            repair_hour_id=repair_hour_id,
            start_hour=RepairHour.hour_validator(start_hour),
            bill=RepairHour.bill_validator(bill)
        )

    @classmethod
    def add_new_service(cls, service_name):
        MechanicServiceProxy.insert_service(RepairHour.service_name_validator(service_name))

    def get_all_busy_hours(self):
        return RepairHourProxy.list_all_busy_hours(self.id)

    def get_all_busy_hours_for_date(self, date):
        return RepairHourProxy.list_all_busy_hours_for_date(RepairHour.date_validator(date),
                                                            self.id)

    def get_all_free_hours(self):
        return RepairHourProxy.list_all_free_hours_for_mechanic(self.id)

    def get_all_free_hours_for_date(self, date):
        return RepairHourProxy.list_all_free_hours_for_mechanic_for_date(RepairHour.date_validator(date), # noqa
                                                                         self.id)

    @classmethod
    def make_mechanic(cls, row):
        return cls(
            id=row[0],
            user_name=row[1],
            email=row[2],
            phone_number=row[3],
            address=row[4],
            title=row[5]
        )

    @classmethod
    def register_and_get(cls, *, user_name, email, phone_number, address, title):
        mechanic = cls(
            id=0,
            user_name=user_name,
            email=email,
            phone_number=phone_number,
            address=address,
            title=title
        )
        mechanic.id = MechanicProxy.insert_mechanic(
            user_name=user_name,
            email=email,
            phone_number=phone_number,
            address=address,
            title=title
        )
        return mechanic
