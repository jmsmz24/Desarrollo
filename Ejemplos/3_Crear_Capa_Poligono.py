#Crear capa de tipo polígono y WGS84 llamada layer en memoria virtual

layer = QgsVectorLayer("Polygon?crs=ESPG:4326","capa","memory")
field = QgsField("id", QVariant.String)
layer.dataProvider().addAttributes([field])

layer.updateFields()

feature = QgsFeature()
feature.setFields(layer.fields())
feature.setAttribute("id","1")

point1 = QgsPointXY(-3.70256, 40.4165) #Madrid
point2 = QgsPointXY(-0.906094, 41.655437) #Zaragoza
point3 = QgsPointXY(2.15899, 41.38879) #Barcelona
point4 = QgsPointXY(2.65024, 39.56939) #Palma de Mallorca
point5 = QgsPointXY(-0.48149, 38.34517) #Alicante

geom = QgsGeometry.fromPolygonXY([[point1,point2,point3,point4,point5]])
feature.setGeometry(geom)
layer.dataProvider().addFeatures([feature])

QgsProject.instance().addMapLayer(layer)