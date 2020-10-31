#Ej1 - Crear puntos aleatorios

#Importatmos el modulo para generar numeros aleatorios
import random

#Creamos una finción donde n es el numero de puntos aleatorios a generar
def createLayer(n):
    #Crear una capa de puntos en la memeoria del equipo
    layer = QgsVectorLayer("Point?crs=ESPG:4326","capa","memory")
    
    #Creamos tres campos
    field1 = QgsField("id", QVariant.Int)
    field2 = QgsField("x_coord", QVariant.Int)
    field3 = QgsField("y_coord", QVariant.Int)
    
    #Añadimos los campos a la capa
    layer.dataProvider().addAttributes([field1, field2, field3])
    
    #Actualizamos campos
    layer.updateFields()
    
    #Generamos una lista de entidades vacía
    features = []
    
    #Generamos un  bucle que repite el proceso de generacion de entidad un número prederminado de veces (parámetro n)
    i=0
    for i in range(n):
        #Creamos entidad
        feature = QgsFeature()
        #Copiamos la misma estructura de campos en la entidad que en la capa layer
        feature.setFields(layer.fields())
        #Generamos x aleatoria en un rango
        x=random.uniform(-19, 5)
        #Generamos y aleatoria en un rango
        y=random.uniform(27, 44)
        #Añadimos valor al campo id
        feature.setAttribute("id",int(i))
        #Añadimos valor al campo x_coord
        feature.setAttribute("x_coord",x)
        #Añadimos valor al campo y_coord
        feature.setAttribute("y_coord",y)
        #Generamos geometria de la entidad
        geom = QgsGeometry.fromPointXY(QgsPointXY(x,y))
        #Añadimos la geometria a la entidad
        feature.setGeometry(geom)
        #Añadimos la entidad a la lista de entidades
        features.append(feature)
        #Imprimimos por consola el id de la entidad
        print("Feature: "+str(i))
    
    #Añadimos la lista de entidades a la capa
    layer.dataProvider().addFeatures(features)

    #Añdimos la capa al lienzo de QGIS
    QgsProject.instance().addMapLayer(layer)

createLayer(100)