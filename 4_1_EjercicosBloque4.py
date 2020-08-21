#Ejercicio 4.1 Obtener coordenadas en CRS EPGS:25830 a partir de las siguientes coordenadas en en CRS EPGS:4236

#Madrid -> -3.70256, 40.4165
#Zaragoza-> -0.906094, 41.655437
#Barcelona -> 2.15899, 41.38879
#Palma de Mallorca-> 2.65024, 39.56939
#Alicante-> -0.48149, 38.34517

#Creamos cinco puntos
point1 = QgsPointXY(-3.70256, 40.4165) #Madrid
point2 = QgsPointXY(-0.906094, 41.655437) #Zaragoza
point3 = QgsPointXY(2.15899, 41.38879) #Barcelona
point4 = QgsPointXY(2.65024, 39.56939) #Palma de Mallorca
point5 = QgsPointXY(-0.48149, 38.34517) #Alicante

#Generamos la geometría de los puntos
geom1 = QgsGeometry.fromPointXY(point1)
geom2 = QgsGeometry.fromPointXY(point2)
geom3 = QgsGeometry.fromPointXY(point3)
geom4 = QgsGeometry.fromPointXY(point4)
geom5 = QgsGeometry.fromPointXY(point5)

#CRS de origen (EPSG:4326) y el CRS destino (EPSG:25830)
epsg4326 = QgsCoordinateReferenceSystem("EPSG:4326")
epsg25830 = QgsCoordinateReferenceSystem("EPSG:25830")

#Creamos transformación
transform = QgsCoordinateTransform(epsg4326, epsg25830, QgsProject.instance())

#A partir del método transform(), realizamos la reproyección de la geometría
geom1.transform(transform)
geom2.transform(transform)
geom3.transform(transform)
geom4.transform(transform)
geom5.transform(transform)

#Imprimimos coordenadas nuevas
print(geom1.asWkt())
print(geom2.asWkt())
print(geom3.asWkt())
print(geom4.asWkt())
print(geom5.asWkt())