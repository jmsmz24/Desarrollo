import Adafruit_DHT 
import os
import time
import psycopg2
import time

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 2)
temp_ambi= round(temperature,1)
hum_ambi= round(humidity,1)

conn = psycopg2.connect('dbname=tempsys')
cur = conn.cursor()

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()	
        return (temp.replace("temp=","").replace("'C",""))
		
def date_today():
		date = time.strftime("%c")
		return (date)
		


insert_query = "INSERT INTO temperaturas (fecha, temp, temperature, humidity) VALUES ('"+date_today()+"',"+measure_temp()+","+str(temp_ambi)+","+str(hum_ambi)+");"
print("Insertando...")
cur.execute(insert_query)
print("Fecha-> "+date_today())
print("Temperatura placa-> "+ measure_temp())
print ("Temperatura sala -> "+ str(temp_ambi))  
print ("Humedad sala -> "+str(hum_ambi))
print("-------------------------------------")
conn.commit()