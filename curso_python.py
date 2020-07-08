#1 PARTE
#1.1.EXPLORAR CAPA VECTORIAL
#------------------------------------------------------------------------------

#Llamar a la capa activa y gardarlo en una variable llamada lyr 
lyr  = iface.activeLayer()

#Obtener propiedades de la capa
lyr.name()
lyr.extent()
lyr.crs()
lyr.dataProvider().storageType()
lyr.dataProvider().dataSourceUri()
lyr.dataProvider().metadata()
lyr.dataProvider().wkbType()


#Obtener todas las entidades con un iterador y guardarlo en una variable llamada features
features = lyr.getFeatures()

#Convertit en lista la variable features
features_list = list(features)

#¿Cunto ENP tenemos en españa?
len(features)

#Obtener el primer elemento de la lista y guardarlo en una variable llamada feature
feature = features_list[0]

#Obtener el nombre del ENP guardado en la variable feature accedendio a su atributo en el campo sitename
feature ["sitename"]



#Obtener la geometria de ENP guardado en la variable feature
feature.geometry()

#Listado del nombre de todos los ENP
[f ["sitename"] for f in features_list]

#Listado de la geometry de todos los ENP
[f.geometry() for f in features_list]

#Suma del area de todos los ENP
sum([f ["area_ha"] for f in features_list])

#Suma del area de todos los ENP solo de extremadura
sum([f ["area_ha"] for f in iface.activeLayer().getFeatures('"ccaa_n_enp"=\'Extremadura\'')])
sum([f ["area_ha"] for f in iface.activeLayer().getFeatures() if f["ccaa_n_enp"]== "Extremadura"])


#Abrir capa

