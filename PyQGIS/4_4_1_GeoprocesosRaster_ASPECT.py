#UD4. Introducción a programación en QGIS3
#4.4.Geoprocesos Raster
#4.4.2. Geoprocesos raster. ASPECT
##################################################

#Capa de entrada (MDT)
input = iface.activeLayer()

#Capa de salida (carpeta, nombre archivo, )
folder = 'C:\\ISM_PyQGIS\\'
name = 'aspect'
format = '.tif'

uri = folder+name+format

parameter_dictionary = {
    'INPUT': input,
    'Z_FACTOR': 1,
    'OUTPUT': uri}
    
result = processing.run("qgis:aspect", parameter_dictionary)
iface.addRasterLayer(uri, name,"gdal")
