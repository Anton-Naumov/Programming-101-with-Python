from models import Projection, session
from controllers.movie_controller import MovieController


class ProjectionController:
    @classmethod
    def add_projection(cls, movie_id, type, date, time):
        if MovieController.check_id(movie_id) is False:
            raise Exception('Movie with id = {} doesn\'t exist!'.format(movie_id))

        session.add(Projection(movie_id, type, date, time))
        session.commit()

    @classmethod
    def get_all_projections_for_movie(cls, movie_id):
        if MovieController.check_id(movie_id) is False:
            return None

        return session.query(Projection).filter(Projection.movie_id == movie_id).\
            order_by(Projection.date).all()

    @classmethod
    def check_id(cls, id):
        return session.query(Projection).filter(Projection.id == id).scalar is not None

    @classmethod
    def check_if_seat_is_taken(cls, projection_id, row, col):
        return session.query(Projection.id).\
            filter(Projection.id == projection_id).\
            filter(Projection.row == row, Projection.col == col).scalar is not None
