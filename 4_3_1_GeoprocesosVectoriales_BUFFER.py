#UD4. Introducción a programación en QGIS3
#4.3.Geoprocesos
#4.3.1. Geoprocesos vectoriales. Buffer
####################################################################################################

#Llamamos a la capa.
lyr  = iface.activeLayer()

#Generamos diccionario de datos con paramentros de entrada
parameter_dictionary = {
    'INPUT':lyr,
    'DISTANCE':5,
    'SEGMENTS':5,
    'END_CAP_STYLE':0,
    'JOIN_STYLE':0,
    'MITER_LIMIT':2,
    'DISSOLVE':False,
    'OUTPUT':'memory:'}

#Ejecutamos el geoporceso buffer
result = processing.run("native:buffer", parameter_dictionary)

#Añadimos la capa al lienzo de QGIS
QgsProject.instance().addMapLayer(result['OUTPUT'])
