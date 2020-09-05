#UD4. Introducción a programación en QGIS3
#4.3.Geoprocesos
#4.3.2. Geoprocesos vectoriales. Dissolve
####################################################################################################

#Generamos diccionario de datos con paramentros de entrada
parameter_dictionary = {
    'INPUT':lyr,
    'FIELD': 'LABEL1', #Disolvemos por el campo type
    'OUTPUT':'memory:'}

#Ejecutamos el geoporceso dissolve
result = processing.run("native:dissolve", parameter_dictionary)

#Añadimos la capa al lienzo de QGIS
QgsProject.instance().addMapLayer(result['OUTPUT'])