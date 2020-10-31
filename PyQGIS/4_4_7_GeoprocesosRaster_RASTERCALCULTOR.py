#UD4. Introducción a programación en QGIS3
#4.4.Geoprocesos Raster
#4.4.7. Geoprocesos raster. COMBINE

raster1=QgsProject.instance().mapLayersByName("L8_Banda_5_Infra")[0] 
raster2=QgsProject.instance().mapLayersByName("L8_Banda_4_Red")[0] 


#Capa de salida (carpeta, nombre archivo, )
folder = 'C:\\ISM_PyQGIS\\'
name = 'ndvi'
format = '.tif'

uri = folder+name+format


parameter_dictionary = {
            'CELLSIZE': 0,
            'CRS': None,
            'EXPRESSION': ' ( \"L8_Banda_5_Infra@1\" - \"L8_Banda_4_Red@1\" )  /  ( \"L8_Banda_5_Infra@1\"+\"L8_Banda_4_Red@1\" ) ',
            'EXTENT': None,
            'LAYERS': [raster1,raster2],
            'OUTPUT': uri
      }
    
result = processing.run("qgis:rastercalculator", parameter_dictionary)
iface.addRasterLayer(uri, name,"gdal")