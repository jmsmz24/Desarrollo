#UD4. Introducción a programación en QGIS3
#4.3.Geoprocesos
#4.3.3. Geoprocesos vectoriales. Intersection
##################################################

#Llamamos a la capa de puntos.
input = QgsProject.instance().mapLayersByName("ne_50m_urban_areas")[0] 

#Llamamos a la capa de poligonos
overlay = QgsProject.instance().mapLayersByName("ne_50m_admin_0_countries")[0] 

parameter_dictionary = {
    'INPUT': input,
    'OVERLAY': overlay,
    'INPUT_FIELDS': '',
    'OVERLAY_FIELDS': '',
    'OVERLAY_FIELDS_PREFIX': '',
    'OUTPUT':'memory:'}
    
result = processing.run("native:intersection", parameter_dictionary)
QgsProject.instance().addMapLayer(result['OUTPUT'])
