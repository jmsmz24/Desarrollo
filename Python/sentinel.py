from sentinelsat.sentinel import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import datetime
import json
import psycopg2
import os
import shutil
from datetime import date

year = str((date.today().year)+2)
#######################################################CONEXION CON BASE DE DATOS#######################################
print("Conectando")

try:
	conn = psycopg2.connect(host="localhost",database="sentinel", user="postgres", password="postgres")
	conn.autocommit = True
	cur = conn.cursor()
except Exception as e:
  print("An exception occurred "+e)
 
ids_downloaded = [] 
  
postgreSQL_select_Query_ids = "SELECT id FROM public.tbl_images_downloads;"
cur.execute(postgreSQL_select_Query_ids)
records = cur.fetchall()

for row in records:
	id_image = str(row[0])
	ids_downloaded.append(id_image)

print(ids_downloaded)

postgreSQL_select_Query = "SELECT id, id_project, name, ST_AsText(geom), order_aoi as geom FROM public.geo_aoi WHERE id_project=3;"
cur.execute(postgreSQL_select_Query)
records = cur.fetchall()

for row in records:
	aoi = str(row[0])
	proyecto = str(row[1])
	name = str(row[2])
	geom =str(row[3])
	order_aoi = str(row[4])

	print("AOI - "+aoi)

	directorio = proyecto+"_"+order_aoi+"_"+name
	
	if not os.path.exists("D:\\datos\\Images\\"+directorio):
		os.mkdir("D:\\datos\\Images\\"+directorio)

	##############################################################################################
	# connect to the API
	api = SentinelAPI('josem.sanchezm.ccaa', 'JMSMjmsm2412', 'https://scihub.copernicus.eu/dhus')

	# search by polygon, time, and Hub query keywords
	#footprint = geojson_to_wkt(read_geojson(geom))

	products = api.query(geom, platformname = 'Sentinel-2', cloudcoverpercentage = (0, 25),producttype='S2MSI1C',beginPosition='[2019-01-01T00:00:00.000Z TO '+year+'-01-01T23:59:59.999Z]')
	json = api.to_geojson(products)

	for i in json["features"]:
		title = i['properties']['title']
		summary = i['properties']['summary']
		ingestiondate = i['properties']['ingestiondate']
		beginposition = i['properties']['beginposition']
		endposition = i['properties']['endposition']
		orbitnumber = str(i['properties']['orbitnumber'])
		relativeorbitnumber = str(i['properties']['relativeorbitnumber'])
		cloudcoverpercentage = str(i['properties']['cloudcoverpercentage'])
		filename = i['properties']['filename']
		format = i['properties']['format']
		identifier = i['properties']['identifier']
		instrumentshortname = i['properties']['instrumentshortname']
		instrumentname = i['properties']['instrumentname']
		s2datatakeid = i['properties']['s2datatakeid']
		platformidentifier = i['properties']['platformidentifier']
		orbitdirection = i['properties']['orbitdirection']
		platformserialidentifier = i['properties']['platformserialidentifier']
		processingbaseline = i['properties']['processingbaseline']
		processinglevel = i['properties']['processinglevel']
		producttype = i['properties']['producttype']
		platformname = i['properties']['platformname']
		size = i['properties']['size']
		uuid = i['properties']['uuid']
		id = i['properties']['id']
		
		if (id not in ids_downloaded):
			print ('no esta')
			product = api.query(geom,uuid=uuid)
			try:
				api.download_all(product)
			except Exception as e:
				print("An exception occurred "+e)

			filename = title+".zip"
			src = "D:\\datos\\"
			dst = "D:\\datos\\Images\\"+directorio+"\\"
			shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
			cur.execute("INSERT INTO tbl_images_downloads (id, beginposition, uuid, title, summary, ingestiondate, endposition, orbitnumber, relativeorbitnumber, cloudcoverpercentage, filename, format, identifier, instrumentshortname, instrumentname, s2datatakeid, platformidentifier, orbitdirection, platformserialidentifier, processingbaseline, processinglevel, producttype, platformname, size, aoi, date_insert,path) VALUES('"+id+"','"+beginposition+"','"+uuid+"', '"+title+"','"+summary+"','"+ingestiondate+"','"+endposition+"',"+orbitnumber+", "+relativeorbitnumber+","+cloudcoverpercentage+", '"+filename+"','"+format+"', '"+identifier+"', '"+instrumentshortname+"','"+instrumentname+"','"+s2datatakeid+"','"+platformidentifier+"','"+orbitdirection+"', '"+platformserialidentifier+"', '"+processingbaseline+"','"+processinglevel+"','"+producttype+"','"+platformname+"', '"+size+"', '"+aoi+"',NOW(), '"+str(os.path.join(dst, filename))+"');")
