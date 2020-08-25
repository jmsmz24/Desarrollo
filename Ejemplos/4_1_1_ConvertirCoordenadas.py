#Ejercicio 4.1 Obtener coordenadas en CRS EPGS:25830 a partir de las siguientes coordenadas en en CRS EPGS:4236

#Madrid -> -3.70256, 40.4165
#Zaragoza-> -0.906094, 41.655437
#Barcelona -> 2.15899, 41.38879
#Palma de Mallorca-> 2.65024, 39.56939
#Alicante-> -0.48149, 38.34517

#CRS de origen (EPSG:4326) y el CRS destino (EPSG:25830)
epsg4326 = QgsCoordinateReferenceSystem("EPSG:4326")
epsg25830 = QgsCoordinateReferenceSystem("EPSG:25830")

#Creamos transformación
transform = QgsCoordinateTransform(epsg4326, epsg25830, QgsProject.instance())

#Creamos listado de coordenadas
coord_list = [(-3.70256, 40.4165),(-0.906094, 41.655437),(2.15899, 41.38879), (2.65024, 39.56939),(-0.48149, 38.34517)]

#Iterador de la lista de coordenadas para generar geometrias
for i in coord_list:
    #Creamos punto
    point = QgsPointXY(i[0],i[1])
    #Generamos la geometría del punto
    geom = QgsGeometry.fromPointXY(point)
    #A partir del método transform(), realizamos la reproyección de la geometría
    geom.transform(transform)
    #Imprimimos coordenadas nuevas
    print(geom.asWkt())
    
    
