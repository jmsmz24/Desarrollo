#Crear capa de tipo punto y WGS84 llamada layer en memoria virtual

layer = QgsVectorLayer("Point?crs=ESPG:4326","capa","memory")
field = QgsField("id", QVariant.String)
layer.dataProvider().addAttributes([field])

layer.updateFields()

feature = QgsFeature()
feature.setFields(layer.fields())
feature.setAttribute("id","1")

point = QgsPointXY(-3.70256, 40.4165)

geom = QgsGeometry.fromPointXY(point)
feature.setGeometry(geom)
layer.dataProvider().addFeatures([feature])

QgsProject.instance().addMapLayer(layer)