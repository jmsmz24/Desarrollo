#UD4. Introducción a programación en QGIS3
#4.2. Selección por atributos y selección por localización
#4.2.2. Selección por atributos
####################################################################################################

#Llamamos a la capa de puntos.
point = QgsProject.instance().mapLayersByName("ne_10m_airports")[0] 

#Llamamos a la capa de poligonos
polygon = QgsProject.instance().mapLayersByName("ne_110m_admin_0_countries")[0] 

#Ejecutamos el geoporceso seleccion por localización
processing.run("native:selectbylocation", {'INPUT':point,'PREDICATE':[0],'INTERSECT':polygon,'METHOD':0}) 
