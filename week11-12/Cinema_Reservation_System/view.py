from exceptions import CancelException, SeatError
from controllers.main_controller import MainController
from controllers.movie_controller import MovieController


class View:
    start_menu = '1. show movies\n'\
                 '2. show movie projections <movie_id>\n'\
                 '3. make reservation'

    def __init__(self):
        self.user = None

    def start(self):
        self.show_start_menu()

    def show_start_menu(self):
        command = ''
        while command != 'exit':
            command = input(f'\n{self.start_menu}\n\nOption:\n>>>')

            if command == '1':
                MainController.show_movies()
            elif command == '2':
                movie_id = input('Movie_id >>>')
                if movie_id.isdigit() is False or MovieController.check_id(int(movie_id)) is False:
                    print('Invalid movie ID!')
                else:
                    MainController.show_movie_projections(int(movie_id))
            elif command == '3':
                try:
                    self.make_reservation_menu()
                except CancelException as e:
                    print('The reservation was canceled!')
            elif command != 'exit':
                print('Invalid option!')

    def login_register_menu(self):
        while self.user is None:
            print('You need to be a user in the system to make reservations!')
            print('1. login\n2. register\n3. cancel')
            command = input('>>>')

            if command == '1':
                self.user = MainController.login()
            elif command == '2':
                self.user = MainController.register()
            elif command == '3':
                break
            else:
                print('Invalid command!')

    @classmethod
    def get_number_input(cls, msg, is_valid_number):
        number = ''
        while number.isdigit() is False or is_valid_number(number) is False:
            if number == 'cancel':
                raise CancelException('The operation was canceled!')

            number = input(msg)

        return number

    def make_reservation_menu(self):
        self.login_register_menu()
        if self.user is None:
            return

        print(f'Hello, {self.user.username}')

        MainController.show_movies()
        movie_id = self.get_number_input('Movie ID >>> ', MovieController.check_id)

        number_of_tickets = self.get_number_input('Number of tickets >>> ', lambda x: int(x) > 0)

        MainController.show_movie_projections(movie_id)
        projection_id = self.get_number_input('Choose a projection >>> ',
                                              lambda p_id:
                                              MovieController.check_id_for_projection(movie_id, int(p_id)))

        self.pick_seats_menu(projection_id, number_of_tickets)

        self.finalize_menu()

    def pick_seats_menu(self, projection_id, number_of_tickets):
        seat_number = 1
        seats_taken = []
        number_of_tickets = int(number_of_tickets)
        while number_of_tickets > 0:
            MainController.show_all_taken_seets_for_projection(projection_id, seats_taken)
            seat = input(f'Choose seat {seat_number}>> ')

            if seat == 'cancel':
                raise CancelException('The operation was canceled!')

            try:
                seats_taken.append(MainController.save_seat(self.user.id, projection_id, seat))
                number_of_tickets -= 1
                seat_number += 1
            except SeatError as e:
                print(str(e))

    def finalize_menu(self):
        final = input('(Confirm - type "finalize" or to exit "give up") >')

        if final == 'finalize':
            MainController.save_seat_finalize()
        else:
            print('The reservation weren\'t saved!')
            # MainController.rollback()

    @classmethod
    def show_table(cls, rows, headers):
        from tabulate import tabulate

        print(tabulate(rows, headers=headers, tablefmt='orgtbl'))

    @classmethod
    def show_message(cls, message):
        print(message)

    @classmethod
    def take_input(cls, msg):
        return input(msg)
