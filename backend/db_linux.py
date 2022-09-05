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


#======================================== Here create water table 
class water_date (base):

    __tablename__ = 'water_use'

    id = Column(Integer, primary_key=True)
    value = Column(Integer)
    datatime = Column(DateTime, default=datetime.utcnow())


    def __init__(self,value):
        self.value = value


#======================================== Here create pump table 

class pump_date (base):

    __tablename__ = 'pump_use'

    id = Column(Integer, primary_key=True)
    value = Column(Integer)
    datatime = Column(DateTime, default=datetime.utcnow())


    def __init__(self,value):
        self.value = value


#======================================== Here create solar table 
class solar_date (base):

    __tablename__ = 'solar_use'

    id = Column(Integer, primary_key=True)
    value = Column(Integer)
    datatime = Column(DateTime, default=datetime.utcnow())


    def __init__(self,value):
        self.value = value
        


base.metadata.create_all(engine)


