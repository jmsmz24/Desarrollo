#Ejemplo 4.3. Crear y Reproyectar capa puntos

#Capa de entrada con el CRS de partida
layer = QgsVectorLayer("Point?crs=EPSG:4326","capa_entrada","memory")

#Capa de salida con el CRS de salida
layer_rep = QgsVectorLayer("Point?crs=EPSG:25830","capa_salida","memory")

#Generamos campos
field1 = QgsField("id", QVariant.String)
field2 = QgsField("x", QVariant.Double)
field3 = QgsField("y", QVariant.Double)

#Añadimos campos y actualizamos a capa de entrada y salida
layer.dataProvider().addAttributes([field1,field2,field3])
layer.updateFields()
layer_rep.dataProvider().addAttributes([field1,field2,field3])
layer_rep.updateFields()

#Listado de coordenadas
coord_list = [(-3.70256, 40.4165),(-0.906094, 41.655437),(2.15899, 41.38879), (2.65024, 39.56939),(-0.48149, 38.34517)]

#Iterador de la lista de coordenadas para generar entidades
count=0
for i in coord_list:
    count +=1
    #Generamos Entidas
    feature = QgsFeature()
    
    #Añadimos Atributos
    feature.setFields(layer.fields())
    feature.setAttribute("id",str(count))
    feature.setAttribute("x",i[0])
    feature.setAttribute("y",i[1])
    
    #Añadimos geometria
    point = QgsPointXY(i[0],i[1])
    geom = QgsGeometry.fromPointXY(point)
    feature.setGeometry(geom)
    print(feature["id"]+" - "+geom.asWkt())
    
    #Añadimos entidades a la capa
    layer.dataProvider().addFeatures([feature])

#Añadimos al lienzo de QGIS la capa layer
QgsProject.instance().addMapLayer(layer)

#Creamos dos objetos con los CSR de entrada y de salida
epsg4326 = QgsCoordinateReferenceSystem("EPSG:4326")
epsg25830 = QgsCoordinateReferenceSystem("EPSG:25830")

#Generamos la transformación del CRS de entrada al CRS de salida
transform = QgsCoordinateTransform(epsg4326, epsg25830, QgsProject.instance())

#Listamos las entidades
features = layer.getFeatures()
features = list(features)

#Iteramos las entidades de la capa de entrada layer, las reproyectamos y la insertamos en la capa de salida layer_rep
count=0
for feature in features:
    count +=1
    
    geom = feature.geometry()
    geom.transform(transform)
    print(feature["id"]+" - "+geom.asWkt())
    
    feature = QgsFeature()
    feature.setFields(layer_rep.fields())
    feature.setAttribute("id",str(count) )
    feature.setAttribute("x",geom.asPoint().x())
    feature.setAttribute("y",geom.asPoint().y())
    feature.setGeometry(geom)
    layer_rep.dataProvider().addFeatures([feature])

#Añadimos al lienzo de QGIS la capa layer
QgsProject.instance().addMapLayer(layer_rep)


    



