#Ejercicio 4.2. Reproyectar capa

#Llamar a la capa activa y gardarlo en una variable llamada layer 
layer  = iface.activeLayer()

#Capa de salida con el CRS de salida
layer_rep = QgsVectorLayer("MultiPolygon?crs=EPSG:25830","capa_salida","memory")

#Obtener todas las entidades con un iterador y guardarlo en una variable llamada features
features = layer.getFeatures()

#Convertit en lista la variable features
features = list(features)

#Creamos dos objetos con los CSR de entrada y de salida
epsg4326 = QgsCoordinateReferenceSystem("EPSG:4326")
epsg25830 = QgsCoordinateReferenceSystem("EPSG:25830")

#Generamos la transformación del CRS de entrada al CRS de salida
transform = QgsCoordinateTransform(epsg4326, epsg25830, QgsProject.instance())

for feature in features:
    geom = feature.geometry()
    geom.transform(transform)
    
    feature_rep = QgsFeature()
    feature_rep.setGeometry(geom)
    
    #Añadimos entidades a la capa
    layer_rep.dataProvider().addFeatures([feature])

#Añadimos al lienzo de QGIS la capa layer
QgsProject.instance().addMapLayer(layer_rep)
    
    

