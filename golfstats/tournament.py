from sqlalchemy import Column, Integer, String
from golfstats import Base

class Tournament(Base):
    __tablename__ = 'tournaments'

    id = Column(String, primary_key=True)
    event_name = Column(String)
    date = Column(String)
    event_url = Column(String)
