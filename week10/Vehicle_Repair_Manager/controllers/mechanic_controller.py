from utils import catch_and_print_exception
from models.mechanic import Mechanic
from models.repair_hour import RepairHour
from controllers.menu_controller import MenuController
from models.exceptions import InvalidDate
from models.exceptions import InvalidIndex
from models.exceptions import InvalidRepairHourData
from models.exceptions import NotValidUserInformation


class MechanicController(MenuController):
    MENU = """
list_all_free_hours
list_free_hours <date>
list_all_busy_hours
list_busy_hours <date>
add_new_repair_hour
add_new_service
update_repair_hour <hour_id>
exit
    """

    def __init__(self, mechanic):
        if isinstance(mechanic, Mechanic) is False:
            raise TypeError('')

        self.mechanic = mechanic
        self.options = {
            'list_all_free_hours': self.list_all_free_hours,
            'list_free_hours': self.list_free_hours_for_date,
            'list_all_busy_hours': self.list_all_busy_hours,
            'list_busy_hours': self.list_all_busy_hours_for_date,
            'add_new_repair_hour': self.add_new_repair_hour,
            'add_new_service': self.add_new_service,
            'update_repair_hour': self.update_repair_hour_mechanic,
            'exit': self.exit
        }

    def list_all_free_hours(self):
        self.print_hours(self.mechanic.get_all_free_hours())

    @catch_and_print_exception(InvalidDate)
    def list_free_hours_for_date(self):
        date = self._read('Date:\n>>>')
        try:
            free_hours_for_date = self.mechanic.get_all_free_hours_for_date(date)
            self.print_hours(free_hours_for_date)
        except InvalidDate as e:
            self._print(str(e))

    def list_all_busy_hours(self):
        self.print_hours(self.mechanic.get_all_busy_hours())

    def list_all_busy_hours_for_date(self):
        date = self._read('Date:\n>>>')
        try:
            busy_hours_for_date = self.mechanic.get_all_busy_hours_for_date(date)
            self.print_hours(busy_hours_for_date)
        except InvalidDate as e:
            self._print(str(e))

    @catch_and_print_exception(InvalidRepairHourData)
    def add_new_repair_hour(self):
        date = self._read('Repair hour date:\n>>>')
        start_hour = self._read('Start hour:\n>>>')
        bill = self._read('Bill:\n>>>')

        self.mechanic.add_new_repair_hour(date=date, start_hour=start_hour, bill=bill)

        self._print('Your created new repair_hour!')
        self.list_all_free_hours()

    @classmethod
    @catch_and_print_exception(InvalidRepairHourData)
    def add_new_service(self):
        service_name = self._read('Provide New service name:\n>>>')

        Mechanic.add_new_service(service_name)

    @catch_and_print_exception(NotValidUserInformation)
    @catch_and_print_exception(InvalidIndex)
    def update_repair_hour_mechanic(self):
        busy_hours = self.mechanic.get_all_free_hours()
        self.print_hours(busy_hours)

        hour_id = self._read('Hour id:\n>>>')
        start_hour = self._read('Start hour:\n>>>')
        bill = self._read('Bill:\n>>>')

        self.validate_id(hour_id, len(busy_hours))
        Mechanic.update_repair_hour(
            repair_hour_id=busy_hours[int(hour_id) - 1][0],
            start_hour=start_hour,
            bill=bill
        )
