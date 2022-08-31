from email.policy import default
from sqlite3 import Date, Time
import mysql.connector
import pymysql
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from datetime import date,datetime,timedelta


dbuser = 'maczo_all'
dbpass = 'Pomidor123!!!'
dbhost = '178.79.191.194'
dbname = 'hotelowa_db'




engine = create_engine(f"mysql+pymysql://{dbuser}:{dbpass}@{dbhost}/{dbname}", echo=True)

base = declarative_base()


class test_class (base):

    __tablename__ = 'test_table69'

    id = Column(Integer, primary_key=True)
    test_name = Column(String(100))
    test_int = Column(Integer)
    test_int2 = Column(Integer)
    datatime = Column(DateTime, default=datetime.utcnow)


    def __init__(self,test_name,test_int, test_int2):
        self.test_int = test_int
        self.test_name = test_name
        self.test_int2 = test_int2


base.metadata.create_all(engine)


