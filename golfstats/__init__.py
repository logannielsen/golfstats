from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:////Users/logannielsen/golfstats/golfstats/golfstats.db', echo=True, encoding='utf8')

Base = declarative_base()

Session = sessionmaker(bind=engine)

from .tournament import Tournament
from .player import GolfPlayer
