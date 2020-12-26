import csv

layer = QgsVectorLayer("Point?crs=ESPG:4326","capa","memory")

field1 = QgsField("code", QVariant.String)
field2 = QgsField("latitude", QVariant.Double)
field3 = QgsField("longitude", QVariant.Double)
field4 = QgsField("name", QVariant.String)

#Añadimos los campos a la capa
layer.dataProvider().addAttributes([field1, field2, field3, field4])
    
#Actualizamos campos
layer.updateFields()

with open('C:\\DesarrolloRepo\\PyQGIS\\Ejemplos\\contries.csv', encoding='latin1') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    for row in csvreader:
        
        code = str(row[0])
        long = float(row[1])
        lat = float(row[2])
        name = str(row[3])
        print(code+" - "+name)
        
        ##Creamos entidad
        feature = QgsFeature()
        #Copiamos la misma estructura de campos en la entidad que en la capa layer
        feature.setFields(layer.fields())
        #Añadimos valor al campo code
        feature.setAttribute("code",code)
        #Añadimos valor al campo x_coord
        feature.setAttribute("latitude",lat)
        #Añadimos valor al campo y_coord
        feature.setAttribute("longitude",long)
        #Añadimos valor al campo name
        feature.setAttribute("name",name)
        #Generamos geometria de la entidad
        geom = QgsGeometry.fromPointXY(QgsPointXY(lat,long))
        #Añadimos la geometria a la entidad
        feature.setGeometry(geom)
        
        layer.dataProvider().addFeatures([feature])
        #Añdimos la capa al lienzo de QGIS
        
    QgsProject.instance().addMapLayer(layer)