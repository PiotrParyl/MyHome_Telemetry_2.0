
import os 
import requests
from dotenv import load_dotenv

load_dotenv()

solaredge = 'https://monitoringapi.solaredge.com/%20site/'+ os.getenv('site_id') + '/overview.json?api_key=' + os.getenv('api_key')
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
    

print(solaredge.solardata()['currentpower'])