import os
import time
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.SistemaPi

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=","").replace("'C",""))
		
def date_today():
		date = time.strftime("%c")
		return (date)
		
def getCPUuse():
    return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))
	
def getDiskSpace():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i +1
        line = p.readline()
        if i==2:
            return(line.split()[1:5])
			
def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])


db.temperatura.insert({"temperatura":float(measure_temp()),"fecha":date_today(),"CPUuse":getCPUuse(),"DiskSpace":getDiskSpace(),"RAMinfo":getRAMinfo()})
print("Insertando...")
print("Fecha-> "+date_today())
print("Temperatura placa-> "+measure_temp())
print("CPUuse-> "+getCPUuse())
print(getDiskSpace())
print(getRAMinfo())
print("-------------------------------------")

       