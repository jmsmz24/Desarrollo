import processing

url= "https://cnecovid.isciii.es/covid19/resources/casos_diagnostico_provincia.csv"
csv = QgsVectorLayer(url, 'datos_covid', 'ogr')

csv.setSubsetString('fecha'' =\'2021-01-18\'')

#QgsProject.instance().addMapLayer(csv)

shp = QgsProject.instance().mapLayersByName("provincias")[0]

shpField='codigo'
csvField='provincia_iso'

parameter_dictionary = {
 'INPUT': shp,
 'FIELD': shpField,
 'INPUT_2': csv,
 'FIELD_2':csvField,
 'METHOD': 0,
 'OUTPUT':'memory:'}

result = processing.runAndLoadResults("qgis:joinattributestable", parameter_dictionary)

