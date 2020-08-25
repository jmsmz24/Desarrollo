#UD4. Introducción a programación en QGIS3
#4.2. Selección por atributos y selección por localización
#4.2.1. Selección por atributos
####################################################################################################

#Llamamos a la capa activa y guardándolo en una variable llamada lyr.
layer = iface.activeLayer()

#Seleccionar todas las entidades de una capa vectorial usando el método selectAll de la clase QgsVectorLayer.
layer.selectAll()

#Seleccionar entidades a través deuna lista de FID con el método select() de la clase QgsVectorLayer.
selectid = [11, 34, 102, 132, 145]
layer.select(selectid)

#Seleccionar según los valores de los atributos con el método selectByExpression de la clase QgsVectorLayer
layer.selectByExpression('"CONTINENT" =\'Europe\'')
layer.selectByExpression('"POP_EST" >50000000')