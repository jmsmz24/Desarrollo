#Ej1 - Suma de area por CCAA

#Referencia a la capa cargada actualmente
layer = iface.activeLayer()

#Referencia a todas las entidades de una capa
features = layer.getFeatures()

#Creamos un diccionario de datos key-value vacío.
totalArea = {} 

#Iterados de cada una de las entidades
for feature in features:
    #Trabajamos con estos campos
    ccaa = feature["NAME_1"]#Comunidad Autonoma (CCAA)
    area = feature["area"]
    
    #Se rellenan los datos de Comunidad Autonoma y Area en parejas clave-valor ({'ccaa':area}) si el area en mayor de 0
    if area > 0

        #Si en el diccionario totalArea ya existe alguna pareja con la CCAA que se va a insertar, se suma el área al valor de la pareja existente
        if ccaa in totalArea:
            totalArea[ccaa] += area
        #Si en el diccionario totalArea NO existe ninguna pareja con la CCAA que se va a insertar, se inserta el valor del area
        else:
            totalArea[ccaa] = area
            
print (totalArea)