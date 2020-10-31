
import os
import time
import psycopg2

conn = psycopg2.connect('dbname=tempsys')
cur = conn.cursor()

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
				
        return (temp.replace("temp=","").replace("'C",""))
		
def date_today():

		date = time.strftime("%c")
		
		return (date)
		
		

while True:
		insert_query = "INSERT INTO temperaturas (fecha, temp) VALUES ('"+date_today()+"',"+measure_temp()+")"
		print("Insertando...")
		cur.execute(insert_query)
		print("Fecha-> "+date_today())
		print("Temperatura placa-> "+measure_temp())
		print("-------------------------------------")
		time.sleep(5)
		conn.commit()

       