#UD3. Introducción a programación en QGIS3
#3.2. Creando capas de puntos, línea y polígono
#3.2.1. Vectorial: Accediendo campos entidades geometrías
####################################################################################################

from statistics import *

#Instancia de QgsProject y guardamos en variable project
project = QgsProject.instance()

#Caracteristicas del proyecto
print(project.absoluteFilePath())
project.absolutePath()
project.baseName()
project.count()
project.crs()
project.distanceUnits()
project.areaUnits()

#Cargar un proyecto
project.read('C:\\ISM_PyQGIS\\01_project.qgs')

#Guardar un proyecto
project.write('C:\\ISM_PyQGIS\\01_project_v2.qgs')

#Llamar a la capa activa y gardarlo en una variable llamada lyr 
lyr  = iface.activeLayer()

#Obtener propiedades de la capa
lyr.name()
lyr.extent()
lyr.crs()
lyr.dataProvider().storageType()
lyr.dataProvider().dataSourceUri()
lyr.dataProvider().metadata()
lyr.dataProvider().wkbType()

#Obtener todas las entidades con un iterador y guardarlo en una variable llamada features
features = lyr.getFeatures()

#Convertit en lista la variable features
features = list(features)

#¿Cuantas entidades tenemos?
len(features)

#Obtener el primer elemento de la lista y guardarlo en una variable llamada feature
feature = features[0]

#Obtener el nombre de la entidad guardada en la variable feature accedendio a su atributo en el campo XXXX
feature ["NAME_2"]

#Obtener la geometria de las entidad guardada en la variable feature
feature.geometry()

#Listado de todss las entidades por el campo XXXX
[feature ["NAME_2"] for feature in features]

#Listado de la geometry de todos las entidades
[feature.geometry() for feature in features]

#Suma del area de todas las entidades
sum([feature ["area"] for feature in features])

#Estadíaticos de las entidades



print(mean([feature ["area"] for feature in features]))
stdev ([feature ["area"] for feature in features])
max ([feature ["area"] for feature in features])
min ([feature ["area"] for feature in features])
median ([feature ["area"] for feature in features])

#Suma del area de todas las entidades filtrado a traves de dos métodos
sum([feature ["area"] for feature in iface.activeLayer().getFeatures('"NAME_1"=\'Castilla y León\'')])#Ejemplo bueno
sum([feature ["area"] for feature in features if feature["NAME_1"]== "Castilla y León"])#Ejemplo malo