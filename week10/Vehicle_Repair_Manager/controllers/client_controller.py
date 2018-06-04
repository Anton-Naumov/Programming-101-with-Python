from models.client import Client
from models.exceptions import NotValidVehicleData
from models.repair_hour import RepairHour
from models.vehicle import Vehicle
from controllers.menu_controller import MenuController
from models.exceptions import InvalidIndex
from models.exceptions import InvalidRepairHourData
from models.exceptions import InvalidDate
from utils import catch_and_print_exception


class ClientController(MenuController):
    MENU = """
list_all_free_hours
list_free_hours <date>
save_repair_hour <hour_id>
update_repair_hour <hour_id>
delete_repair_hour <hour_id>
list_personal_vehicles
add_vehicle
update_vehicle <vehicle_id>
delete_vehicle <vehicle_id>
exit
    """

    def __init__(self, client):
        if isinstance(client, Client) is False:
            raise TypeError('')

        self.client = client
        self.options = {
            'list_all_free_hours': self.list_all_free_hours,
            'list_free_hours': self.list_free_hours_for_date,
            'save_repair_hour': self.save_repair_hour,
            'delete_repair_hour': self.delete_repair_hour,
            'update_repair_hour': self.update_repair_hour,
            'list_personal_vehicles': self.list_personal_vehicles,
            'add_vehicle': self.add_vehicle,
            'update_vehicle': self.update_vehicle,
            'delete_vehicle': self.delete_vehicle,
            'exit': self.exit
        }

    @classmethod
    def list_all_free_hours(self):
        self.print_hours(RepairHour.get_all_free_hours())

    @classmethod
    @catch_and_print_exception(InvalidDate)
    def list_free_hours_for_date(cls):
        date = cls._read('Date:\n>>>')
        try:
            free_hours_for_date = RepairHour.get_all_free_hours_for_date(date)
            cls.print_hours(free_hours_for_date)
        except InvalidDate as e:
            cls._print(str(e))

    def print_vehicles(cls, vehicles):
        to_print = [[pos + 1, str(v)] for pos, v in enumerate(vehicles)]
        cls._print(to_print, ['id', 'Vehicle'])

    def list_personal_vehicles(self):
        self.print_vehicles(self.client.get_personal_vehicles())

    def list_vehicles_and_get_id(self):
        vehicles = self.client.get_personal_vehicles()
        self.print_vehicles(vehicles)
        vehicle_idx = self._read('Vehicle id:\n>>>')

        self.validate_id(vehicle_idx, len(vehicles))
        return vehicles[int(vehicle_idx) - 1].id

    @classmethod
    def list_repair_hours_and_get_id(cls):
        repair_hours = RepairHour.get_all_free_hours()
        cls.print_hours(repair_hours)
        repair_hours_idx = cls._read('Repair hour id:\n>>>')

        cls.validate_id(repair_hours_idx, len(repair_hours))
        return repair_hours[int(repair_hours_idx) - 1][0]

    @catch_and_print_exception(NotValidVehicleData)
    def add_vehicle(self):
        self.client.add_vehicle(
            category=self._read('Category:'),
            make=self._read('Make:'),
            model=self._read('Model:'),
            register_number=self._read('Register number:'),
            gear_box=self._read('Gear box:')
        )

    @catch_and_print_exception(InvalidIndex)
    @catch_and_print_exception(NotValidVehicleData)
    def update_vehicle(self):
        self.client.update_vehicle(
            vehicle_id=self.list_vehicles_and_get_id(),
            category=self._read('Category:'),
            make=self._read('Make:'),
            model=self._read('Model:'),
            register_number=self._read('Register number:'),
            gear_box=self._read('Gear box:')
        )

    @catch_and_print_exception(InvalidIndex)
    def delete_vehicle(self):
        self.client.delete_vehicle(self.list_vehicles_and_get_id())

    @catch_and_print_exception(InvalidIndex)
    @catch_and_print_exception(InvalidRepairHourData)
    def save_repair_hour(self):
        repair_hour_id = self.list_repair_hours_and_get_id()

        vehicle_id = self.list_vehicles_and_get_id()

        services = RepairHour.get_services()
        services = [[pos + 1, service] for pos, service in enumerate(services)]
        self._print(services, ['id', 'Service'])
        service_idx = self._read('Service id:\n>>>')
        self.validate_id(service_idx, len(services))
        service_name = services[int(service_idx) - 1][1]

        Client.save_repair_hour(
            hour_id=repair_hour_id,
            vehicle_id=vehicle_id,
            service_name=service_name
        )

    def list_saved_repair_hours_and_get_hour(self):
        repair_hours = self.client.get_saved_repair_hours()
        repair_hours_with_vehicles = [[pos + 1, v[1], v[2], v[3],
                                      str(Vehicle.make_vehicle(v[4:10]))]
                                      for pos, v in enumerate(repair_hours)]
        self._print(
            repair_hours_with_vehicles,
            headers=['id', 'Date', 'Hour', 'Bill', 'Vehicle'],
        )

        hour_idx = self._read('Hour id:\n>>>')
        self.validate_id(hour_idx, len(repair_hours))
        return repair_hours[int(hour_idx) - 1]

    @catch_and_print_exception(InvalidIndex)
    def delete_repair_hour(self):
        hour_to_delete = self.list_saved_repair_hours_and_get_hour()
        Client.delete_repair_hour(hour_to_delete[0])

    @catch_and_print_exception(InvalidIndex)
    @catch_and_print_exception(InvalidRepairHourData)
    def update_repair_hour(self):
        hour_to_update = self.list_saved_repair_hours_and_get_hour()

        self._print('Choose one of the following:\n'
                    '1 - change start hour\n'
                    '2 - change bill\n'
                    '3 - return to main menu\n')

        option = self._read('>>>')
        start_hour, bill = str(hour_to_update[2]), str(hour_to_update[3])

        if '1' == option:
            start_hour = self._read('New start hour:')
        elif '2' == option:
            bill = self._read('New bill:')
        else:
            return

        Client.update_repair_hour(
            repair_hour_id=hour_to_update[0],
            start_hour=start_hour,
            bill=bill
        )
