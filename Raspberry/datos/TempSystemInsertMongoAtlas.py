import os
import time
from pymongo import MongoClient

	client = MongoClient("mongodb+srv://jmsmz24:jmsmjmsm@cluster0-3qonq.mongodb.net/test")
	db = client.test
	
	
try: db.command("serverStatus")
	except Exception as e: print(e)
	else: print("You are connected!")
	client.close()

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

       