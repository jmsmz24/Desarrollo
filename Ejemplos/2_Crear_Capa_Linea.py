#Crear capa de tipo linea y WGS84 llamada layer en memoria virtual

layer = QgsVectorLayer("LineString?crs=ESPG:4326","capa","memory")
field = QgsField("id", QVariant.String)
layer.dataProvider().addAttributes([field])

layer.updateFields()
feature = QgsFeature()
feature.setFields(layer.fields())
feature.setAttribute("id","1")

point1 = QgsPointXY(-3.70256, 40.4165) #Madrid
point2 = QgsPointXY(-0.906094, 41.655437) #Zaragoza
point3 = QgsPointXY(2.15899, 41.38879) #Barcelona

geom = QgsGeometry.fromPolylineXY([point1, point2, point3])
feature.setGeometry(geom)
layer.dataProvider().addFeatures([feature])

QgsProject.instance().addMapLayer(layer)