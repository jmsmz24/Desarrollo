# connect to the API
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date

user = QInputDialog().getText(None, "User", "User please:")
password = QInputDialog().getText(None, "Password", "Password please:")


api = SentinelAPI(user, password, 'https://scihub.copernicus.eu/dhus')

point = QgsPointXY(-3.70256, 40.4165)
geom = QgsGeometry.fromPointXY(point).asWkt()


products = api.query(geom, platformname = 'Sentinel-2', cloudcoverpercentage = (0, 25),producttype='S2MSI1C',beginPosition='[2020-01-20T00:00:00.000Z TO 2020-02-01T23:59:59.999Z]')
json = api.to_geojson(products)

for i in json["features"]:
    summary = i['properties']['summary']
    print(summary)
    uuid = i['properties']['uuid']
    product = api.query(uuid=uuid)
    api.download_all(product, directory_path='C:\cursos')
    
    


