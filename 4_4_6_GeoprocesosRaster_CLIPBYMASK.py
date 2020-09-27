#UD4. Introducción a programación en QGIS3
#4.4.Geoprocesos Raster
#4.4.6. Geoprocesos raster. CLIP BY MASK
##################################################


input = QgsProject.instance().mapLayersByName("E05-29-13-a")[0] 
mask = QgsProject.instance().mapLayersByName("Mascara")[0] 


#Capa de salida (carpeta, nombre archivo, )
folder = 'C:\\ISM_PyQGIS\\'
name = 'clipbymask'
format = '.tif'

uri = folder+name+format

parameter_dictionary = {
            'INPUT': input,
            'MASK': mask,
            'OPTIONS': '',
            'OUTPUT': uri}
    
result = processing.run("gdal:cliprasterbymasklayer", parameter_dictionary)
iface.addRasterLayer(uri, name,"gdal")