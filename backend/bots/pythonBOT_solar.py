import os 
import requests
from time import sleep, time
import datetime
from datetime import datetime
import db_linux
from sqlalchemy.orm import sessionmaker


#========================= db.connection #=========================
Session = sessionmaker(bind=db_linux.engine)
session = Session()

#========================= licznik connection #=========================

solaredge = 'https://monitoringapi.solaredge.com/%20site/'+ '1215266' + '/overview.json?api_key=' + 'IF60NL1EH3H9NZOFT9XG64LQF0UMDL8Q'
json_data = requests.get(solaredge).json()

class solaredge():
    def solardata():
        lastupdatetime = json_data['overview']['lastUpdateTime']
        totalenergythisyear = json_data['overview']['lifeTimeData']['energy']/1000
        lastyearenergy = json_data['overview']['lastYearData']['energy']/1000
        lastmonthenergy = json_data['overview']['lastMonthData']['energy']/1000
        lastdayenergy = json_data['overview']['lastDayData']['energy']/1000
        currentpower = json_data['overview']['currentPower']['power']
        return {'lastupdatetime':lastupdatetime,'totalenergythisyear': totalenergythisyear,'lastyearenergy': lastyearenergy,'lastmonthenergy': lastmonthenergy,'lastdayenergy': lastdayenergy,'currentpower':currentpower}

#========================= loop #=========================

while True:
    wynik = float(solaredge.solardata()['currentpower'])
    new_data = db_linux.solar_date(wynik)
    session.add(new_data)
    session.commit()
    sleep(300)
