#UD3. Introducción a programación en QGIS3
#3.3. Creando capas de puntos, línea y polígono
#3.3.3.Crear Capa Polígono
####################################################################################################

#Creamos una capa de tipo línea a través de un objeto de tipo QgsVectorLayer que guardamos en la variable layer.
layer = QgsVectorLayer("Polygon?crs=ESPG:4326","capa","memory")

#Creamos un campo de tipo alfanumérico llamado id a través de un objeto de tipo QgsField y lo guardamos en la variable field.
field = QgsField("id", QVariant.String)

#Añadimos el campo creado a la capa layer a través del método addAtributte() de la clase QgsVectorLayer al cual le pasaremos como parámetro de entrada el objeto de tipo QgsField llamado field.
layer.dataProvider().addAttributes([field])

#Refrescamos campos en la capa layer
layer.updateFields()

#Generamos una entidad para posteriormente añadir atributos y geometría, Creamos el objeto de tipo QgsFeature y lo guardamos en una variable llamado feature.
feature = QgsFeature()

#Le damos la misma estructura de campos que el objeto tipo QgsVectorLayer llamado layer.
feature.setFields(layer.fields())

#Añadimos los atributos usando el método setAtributes() de la clase QgsFeature, pasándole como parámetros nombre del campo y  el valor.
feature.setAttribute("id","1")

#Creamos cinco objetos de tipo QgsPointXY y los guardamos en variables llamadas point1, point2 y point3. Estos puntos serán los vértices de la línea que generaremos.
point1 = QgsPointXY(-3.70256, 40.4165) #Madrid
point2 = QgsPointXY(-0.906094, 41.655437) #Zaragoza
point3 = QgsPointXY(2.15899, 41.38879) #Barcelona
point4 = QgsPointXY(2.65024, 39.56939) #Palma de Mallorca
point5 = QgsPointXY(-0.48149, 38.34517) #Alicante

#Generamos la geometría utilizando el método fromPolygonXY () de la clase QgsGeometry, pasándole como parámetro los objetos de tipo QgsPointXY creados anteriormente.
geom = QgsGeometry.fromPolygonXY([[point1,point2,point3,point4,point5]])

#Añadimos la geometría al objeto feature
feature.setGeometry(geom)

#Añadimos finalmente la entidad feature a la capa layer.
layer.dataProvider().addFeatures([feature])

#Añadimos la capa layer a QGIS
QgsProject.instance().addMapLayer(layer)
