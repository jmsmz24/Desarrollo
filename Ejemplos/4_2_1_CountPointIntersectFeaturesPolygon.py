# Capa puntos
point = QgsProject.instance().mapLayersByName("ne_10m_airports")[0] 
# Capa polígonos
polygon = QgsProject.instance().mapLayersByName("ne_110m_admin_0_countries")[0] 

#Campo nombre
field = "ADMIN"
#Fista diccionario
features_list = []

#Iterar entidades capa poligono
features = polygon.getFeatures()
for feature in features:
    name_feature = feature [field]
    polygon.setSubsetString(''+field+' =\''+name_feature+'\'')

    processing.run("native:selectbylocation", {'INPUT':point,'PREDICATE':[0],'INTERSECT':polygon,'METHOD':0}) 
    n_points = point.selectedFeatureCount()
        
    pair ={'Feature':name_feature,'Count':n_points}
    features_list.append(pair)

polygon.setSubsetString('')
print(features_list)

max_value = max(features_list, key=lambda x:x['Count'])
print(max_value)