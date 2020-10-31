#UD4. Introducción a programación en QGIS3
#4.4.Geoprocesos Raster
#4.4.5. Geoprocesos raster. COMBINE
##################################################


raster1=QgsProject.instance().mapLayersByName("E05-29-13-a")[0] 
raster2=QgsProject.instance().mapLayersByName("E05-29-13-b")[0] 


#Capa de salida (carpeta, nombre archivo, )
folder = 'C:\\ISM_PyQGIS\\'
name = 'combine'
format = '.tif'

uri = folder+name+format


parameter_dictionary = {
            'DATA_TYPE': 5,
            'EXTRA': '',
            'INPUT': [raster1,raster2],
            'NODATA_INPUT': None,
            'NODATA_OUTPUT': None,
            'OPTIONS': '',
            'PCT': False,
            'SEPARATE': False,
            'OUTPUT': uri}
    
result = processing.run("gdal:merge", parameter_dictionary)
iface.addRasterLayer(uri, name,"gdal")