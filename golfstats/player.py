from sqlalchemy import Column, Integer, String

from golfstats import Base

class GolfPlayer(Base):

    __tablename__ = 'golfplayers'

    id = Column(Integer, primary_key=True)
    given_name = Column(String)
    surname = Column(String)
    nationality = Column(String)
