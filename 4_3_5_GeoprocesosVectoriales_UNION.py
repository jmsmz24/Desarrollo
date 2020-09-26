#UD4. Introducción a programación en QGIS3
#4.3.Geoprocesos
#4.3.4. Geoprocesos vectoriales. Clip
##################################################

#Capa INPUT.
input = QgsProject.instance().mapLayersByName("ne_10m_admin_1_states_provinces")[0] 

#Capa OVERLAY
overlay = QgsProject.instance().mapLayersByName("Area_recorte")[0] 

parameter_dictionary = {
    'INPUT': input,
    'OVERLAY': overlay,
    'OVERLAY_FIELDS_PREFIX':'',
    'OUTPUT':'memory:'}
    
result = processing.run("native:union", parameter_dictionary)
QgsProject.instance().addMapLayer(result['OUTPUT'])
