import os
import timez
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.SistemaPi

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=","").replace("'C",""))
		
def date_today():
		date = time.strftime("%c")
		return (date)
		
while True:
		db.temperatura.insert({"temperatura":float(measure_temp()),"fecha":date_today()})
		print("Insertando...")
		print("Fecha-> "+date_today())
		print("Temperatura placa-> "+measure_temp())
		print("-------------------------------------")
		time.sleep(5)

       