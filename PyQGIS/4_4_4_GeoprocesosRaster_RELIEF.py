#UD4. Introducción a programación en QGIS3
#4.4.Geoprocesos Raster
#4.4.4. Geoprocesos raster. RELIEVE
##################################################

#Capa de entrada (MDT)
input = iface.activeLayer()

#Capa de salida (carpeta, nombre archivo, )
folder = 'C:\\ISM_PyQGIS\\'
name = 'relief'
format = '.tif'

uri = folder+name+format


parameter_dictionary = {
    'INPUT': input,
    'Z_FACTOR': 1,
    'AUTO_COLORS':True,
    'COLORS':'',
    'OUTPUT': uri}
    
result = processing.run("qgis:relief", parameter_dictionary)
iface.addRasterLayer(uri, name,"gdal")
