from models import Reservation, session
from controllers.projection_controller import ProjectionController
from controllers.user_controller import UserController
from exceptions import SeatError, UserError, ProjectionException


class ReservationController:
    @classmethod
    def save_seat(cls, user_id, projection_id, row, col):
        if UserController.check_id(user_id) is False:
            raise UserError('There is no user with id = {}!'.format(user_id))

        if ProjectionController.check_id(projection_id) is False:
            raise ProjectionException('There is no projection with id = {}!'.
                                      format(projection_id))

        if cls.check_if_seat_is_taken(projection_id, row, col):
            raise SeatError('The seat is taken!')

        session.add(Reservation(
            user_id=user_id,
            projection_id=projection_id,
            row=row,
            col=col)
        )

    @classmethod
    def check_if_seat_is_taken(cls, projection_id, row, col):
        return session.query(Reservation.id).\
            filter(Reservation.projection_id == projection_id).\
            filter(Reservation.row == row, Reservation.col == col).scalar() is not None

    @classmethod
    def get_all_taken_seets_for_projection(cls, projection_id):
        return session.query(Reservation.row, Reservation.col).\
            filter(Reservation.projection_id == projection_id).all()
