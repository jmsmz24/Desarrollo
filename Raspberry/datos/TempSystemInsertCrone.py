import os
import time
import psycopg2
import RPi.GPIO as GPIO
import time
import Adafruit_DHT 

conn = psycopg2.connect('dbname=tempsys')
cur = conn.cursor()

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()	
        return (temp.replace("temp=","").replace("'C",""))
		
def date_today():
		date = time.strftime("%c")
		return (date)
		

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 2)

temp_ambi= round(temperature,2)
hum_ambi= round(humidity,2)
		
#ledPin = 11 # RPI Board pin11


#GPIO.setmode(GPIO.BOARD) # Numbers GPIOs by physical location
#GPIO.setup(ledPin, GPIO.OUT) # Set ledPin's mode is output
#GPIO.output(ledPin, GPIO.LOW) # Set ledPin low to off led
	
#GPIO.output(ledPin, GPIO.HIGH) # led on
#time.sleep(5)
	
insert_query = "INSERT INTO temperaturas (fecha, temp, temperature, humidity) VALUES ('"+date_today()+"',"+measure_temp()+","+str(temp_ambi)+","+str(hum_ambi)+");"
#print("Insertando...")
cur.execute(insert_query)
#print("Fecha-> "+date_today())
#print("Temperatura placa-> "+measure_temp())
#print("-------------------------------------")
conn.commit()

#GPIO.output(ledPin, GPIO.LOW) # led off
