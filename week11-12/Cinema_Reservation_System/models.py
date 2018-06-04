from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Float, Date, Time
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


engine = create_engine("postgresql+psycopg2://anton:@/cinema")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


def initialize_database():
    Base.metadata.create_all(engine)


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    rating = Column(Float)


class Projection(Base):
    __tablename__ = "projections"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey(Movie.id))
    movie = relationship(Movie, backref='projections')
    type = Column(String)
    date = Column(Date)
    time = Column(Time)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)


class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    user = relationship('User', backref='reservations')
    projection_id = Column(Integer, ForeignKey(Projection.id))
    projection = relationship('Projection', backref='reservations')
    row = Column(Integer)
    col = Column(Integer)
