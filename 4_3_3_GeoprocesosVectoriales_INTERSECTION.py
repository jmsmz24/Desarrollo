#UD4. Introducción a programación en QGIS3
#4.3.Geoprocesos
#4.3.3. Geoprocesos vectoriales. Intersection
##################################################

#Llamamos a la capa de puntos.
point = QgsProject.instance().mapLayersByName("ne_10m_airports")[0] 

#Llamamos a la capa de poligonos
polygon = QgsProject.instance().mapLayersByName("ne_110m_admin_0_countries")[0] 

parameter_dictionary = {
    'INPUT': point,
    'OVERLAY': polygon,
    'INPUT_FIELDS': '',
    'OVERLAY_FIELDS': '',
    'OVERLAY_FIELDS_PREFIX': '',
    'OUTPUT':'memory:'}
    
result = processing.run("native:intersection", parameter_dictionary)
QgsProject.instance().addMapLayer(result['OUTPUT'])
