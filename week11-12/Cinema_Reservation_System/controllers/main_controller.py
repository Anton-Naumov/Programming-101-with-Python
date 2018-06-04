from re import match
from models import session
from controllers.user_controller import UserController
from controllers.movie_controller import MovieController
from controllers.projection_controller import ProjectionController
from controllers.reservation_controller import ReservationController
from exceptions import MovieException, InvalidUserInformation, SeatError


class MainController:
    @classmethod
    def show_table(cls, rows, columns_names):
        from view import View
        View.show_table(rows, columns_names)

    @classmethod
    def show_message(cls, message):
        from view import View
        View.show_message(message)

    @classmethod
    def take_input(cls, msg):
        from view import View
        return View.take_input(msg)

    @classmethod
    def show_movies(cls):
        movies = MovieController.get_all_movies()
        rows = [[movie.id, movie.name, movie.rating] for movie in movies]
        cls.show_table(rows, ['ID', 'Movie title', 'rating'])

    @classmethod
    def show_movie_projections(cls, movie_id):
        try:
            movie_name = MovieController.get_movie(movie_id).name
            projections = ProjectionController.get_all_projections_for_movie(movie_id)
        except MovieException:
            raise Exception('Invalid movie id!')

        rows = [[p.id, p.date, p.time, p.type] for p in projections]

        cls.show_message(f'Projections for movie {movie_name}:')
        cls.show_table(rows, ['ID', 'Date', 'Time', 'type'])

    @classmethod
    def login(cls):
        username, password = cls.take_username_and_password()

        try:
            return UserController.login(username, password)
        except InvalidUserInformation as e:
            cls.show_message(str(e))

        return None

    @classmethod
    def register(cls):
        username, password = cls.take_username_and_password()

        try:
            return UserController.register(username, password)
        except InvalidUserInformation as e:
            cls.show_message(str(e))

        return None

    @classmethod
    def take_username_and_password(cls):
        return cls.take_input('Username >>> '), cls.take_input('Password >>> ')

    @classmethod
    def save_seat(cls, user_id, projection_id, seat):
        print(seat[1:-1])
        if match('\(\d{1,2},\d{1,2}\)$', seat) is None:
            raise SeatError('Invalid seat!')

        row, col = seat[1:-1].split(',')
        row, col = int(row), int(col)

        if row < 1 or row > 10 or col < 1 or col > 10:
            raise SeatError('Invalid seat!')

        ReservationController.save_seat(user_id, projection_id, row, col)
        return row, col

    @classmethod
    def show_all_taken_seets_for_projection(cls, projection_id, temporaty_seets):
        taken_seets = ReservationController.get_all_taken_seets_for_projection(projection_id)
        seats = '  1 2 3 4 5 6 7 8 9 10'

        for row in range(1, 11):
            row_string = [str(row)]
            for col in range(1, 11):
                if (row, col) in taken_seets or (row, col) in temporaty_seets:
                    row_string.append('X')
                else:
                    row_string.append('.')
            seats = f'{seats}\n{" ".join(row_string)}'

        cls.show_message(seats)

    @classmethod
    def save_seat_finalize(cls):
        session.commit()

    @classmethod
    def rollback(cls):
        session.rollback()
