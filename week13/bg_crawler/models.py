from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class BgServers(Base):
    __tablename__ = "bgservers"
    id = Column(Integer, primary_key=True)
    page_id = Column(Integer, unique=True)
    server = Column(String)
    url = Column(String)


engine = create_engine("postgresql+psycopg2://anton:@/bg_servers")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
