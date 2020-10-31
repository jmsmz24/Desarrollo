#UD4. Introducción a programación en QGIS3
#4.4.Geoprocesos Raster
#4.4.2. Geoprocesos raster. HILLSHADE
##################################################

#Capa de entrada (MDT)
input = iface.activeLayer()

#Capa de salida (carpeta, nombre archivo, )
folder = 'C:\\ISM_PyQGIS\\'
name = 'hillshade'
format = '.tif'

uri = folder+name+format

parameter_dictionary = {
    'INPUT': input,
    'Z_FACTOR': 1,
    'AZIMUTH': 45,
    'V_ANGLE':45,
    'OUTPUT': uri}
    
result = processing.run("qgis:hillshade", parameter_dictionary)
iface.addRasterLayer(uri, name,"gdal")
