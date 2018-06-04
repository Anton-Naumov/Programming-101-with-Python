from models import Movie, session
from exceptions import MovieException


class MovieController:
    @classmethod
    def add_movie(cls, name, rating):
        session.add(Movie(name=name, rating=rating))
        session.commit()

    @classmethod
    def get_movie(cls, id):
        if cls.check_id(id) is False:
            raise MovieException('Movie with id = {} doesn\'t exist'.format(id))
        return session.query(Movie).filter(Movie.id == id).one()

    @classmethod
    def get_all_movies(cls):
        return session.query(Movie).all()

    @classmethod
    def check_id(cls, id):
        return session.query(Movie.id).filter(Movie.id == id).scalar() is not None

    @classmethod
    def get_all_movies_ordered_by_rating(cls):
        return session.query(Movie).order_by(Movie.rating).all()

    @classmethod
    def check_id_for_projection(cls, movie_id, projection_id):
        from controllers.projection_controller import ProjectionController
        projections = ProjectionController.get_all_projections_for_movie(movie_id)

        return any([projection.id == projection_id for projection in projections])
