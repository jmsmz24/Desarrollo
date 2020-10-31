#UD4. Introducción a programación en QGIS3
#4.3.Geoprocesos
#4.3.4. Geoprocesos vectoriales. Clip
##################################################

#Capa INPUT.
input = QgsProject.instance().mapLayersByName("CLC_CAM")[0] 

#Capa OVERLAY
overlay = QgsProject.instance().mapLayersByName("LimiteSierraGuadarrama")[0] 

parameter_dictionary = {
    'INPUT': input,
    'OVERLAY': overlay,
    'OUTPUT':'memory:'}
    
result = processing.run("native:clip", parameter_dictionary)
QgsProject.instance().addMapLayer(result['OUTPUT'])
