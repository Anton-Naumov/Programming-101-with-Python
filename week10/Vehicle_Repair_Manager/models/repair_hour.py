import re
from models.proxys.repair_hour_proxy import RepairHourProxy
from models.exceptions import InvalidDate
from models.exceptions import InvalidRepairHourData
from models.proxys.mechanic_service_proxy import MechanicServiceProxy


class RepairHour:
    @classmethod
    def date_validator(cls, date):
        if re.match('\d{2}-\d{2}-\d{4}$', date) is None:
            raise InvalidDate('The date format is DD-MM-YYYY!')
        return date

    @classmethod
    def hour_validator(cls, hour):
        if re.match('\d{1,2}:\d{2}$', hour) is None:
            raise InvalidRepairHourData('Invalid hour! The hour format is HH:MM!')

        hours, minutes = hour.split(':')

        if int(hours) > 24 or int(minutes) > 60:
            raise InvalidRepairHourData('Invalid hour!')
        return hour

    @classmethod
    def bill_validator(cls, bill):
        if len(bill) > 10 or re.match('[1-9][0-9]*(.[0-9]{1,2})?$', bill) is None:
            raise InvalidRepairHourData('Invalid bill!')
        return bill

    @classmethod
    def service_name_validator(cls, service_name):
        if service_name == '' or len(service_name) > 30:
            raise InvalidRepairHourData('Invalid service_name!')
        return service_name

    @classmethod
    def get_all_free_hours(cls):
        return RepairHourProxy.list_all_free_hours()

    @classmethod
    def get_all_free_hours_for_date(cls, date):
        return RepairHourProxy.list_all_free_hours_for_date(cls.date_validator(date))

    @classmethod
    def get_services(cls):
        return MechanicServiceProxy.query_all_services()
