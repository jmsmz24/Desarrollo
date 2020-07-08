#1 PRINCIPIOS BÁSICOS PyQGIS
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

#¿Cuantas entidades tenemos?
len(features_list)

#Obtener el primer elemento de la lista y guardarlo en una variable llamada feature
feature = features_list[0]

#Obtener el nombre de la entidad guardada en la variable feature accedendio a su atributo en el campo XXXX
feature ["sitename"]

#Obtener la geometria de las entidad guardada en la variable feature
feature.geometry()

#Listado de todss las entidades por el campo XXXX
[f ["sitename"] for f in features_list]

#Listado de la geometry de todos las entidades
[f.geometry() for f in features_list]

#Suma del area de todas las entidades
sum([f ["area_ha"] for f in features_list])

#Suma del area de todas las entidades filtrado a traves de dos métodos
sum([f ["area_ha"] for f in iface.activeLayer().getFeatures('"ccaa_n_enp"=\'Extremadura\'')]) #Ejemplo bueno
sum([f ["area_ha"] for f in iface.activeLayer().getFeatures() if f["ccaa_n_enp"]== "Extremadura"]) #Ejemplo malo
