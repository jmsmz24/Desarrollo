#UD4. Introducción a programación en QGIS3
#4.1. Proyecciones y reproyecciones
#4.1.1. Reproyecion de una capa
####################################################################################################

#Capa de entrada con el CRS de partida
layer = QgsVectorLayer("Point?crs=EPSG:4326","capa","memory")

#Capa de salida con el CRS de salida
layer_rep = QgsVectorLayer("Point?crs=EPSG:25830","capa","memory")

#Imprimimos en pantalla CRS de la capa de entrada layer
crs_layer = layer.crs().authid()
print(crs_layer)

#Creamos campos
field1 = QgsField("id", QVariant.String)
field2 = QgsField("ciudad", QVariant.String)
field3 = QgsField("long_4326", QVariant.Double)
field4 = QgsField("lat_4326", QVariant.Double)
field5 = QgsField("x_25830", QVariant.Double)
field6 = QgsField("y_25830", QVariant.Double)

#Añadimos los campos creados a la capa layer
layer_rep.dataProvider().addAttributes([field1,field2,field3,field4,field5,field6])

#Refrescamos campos en la capa layer
layer_rep.updateFields()

#Generamos una entidad
feature = QgsFeature()

#Generamos punto
point = QgsPointXY(-3.70256, 40.4165)
#Generamos geometria a traves del punto
geom = QgsGeometry.fromPointXY(point)
#Asignamos la geometria a la entidad
feature.setGeometry(geom)
#Añadimos la entidad a la capa de entrada layer
layer.dataProvider().addFeatures([feature])

#Hacemos una lista iterable con todas las entidades
features = layer.getFeatures()
features = list(features)

#Imprimimos por pantalla las coordenadas de las geometrias de la capa de entrada layer
for feature in features:
    print(feature.geometry().asWkt())

#Creamos dos objetos con los CSR de entrada y de salida
epsg4326 = QgsCoordinateReferenceSystem("EPSG:4326")
epsg25830 = QgsCoordinateReferenceSystem("EPSG:25830")

#Generamos la transformación del CRS de entrada al CRS de salida
transform = QgsCoordinateTransform(epsg4326, epsg25830, QgsProject.instance())

#Iteramos las entidades de la capa de entrada layer, las reproyectamos y la insertamos en la capa de salida layer_rep
for feature in features:
    geom = feature.geometry()
    geom.transform(transform)
    print(geom.asWkt())
    
    feature = QgsFeature()
    feature.setGeometry(geom)
    layer_rep.dataProvider().addFeatures([feature])

#Imprimimos en pantalla CRS de la capa de salida layer_rep
crs_layer_rep = layer_rep.crs().authid()
print(crs_layer_rep)

#Añadimos al lienzo de QGIS la capa layer_rep
QgsProject.instance().addMapLayer(layer_rep)