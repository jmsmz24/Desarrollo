# Capa polígonos
polygon = QgsProject.instance().mapLayersByName("ne_110m_admin_0_countries")[0] 

#Iterar entidades capa poligono
features = polygon.getFeatures()

for feature in features:
    polygon.removeSelection()
    fid = feature.id()
    name = feature ["ADMIN"]
    polygon.select(fid)
    file_name = str(fid)+"_"+name
    fn = 'C:/data/'+file_name+'.shp'
    writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn, 'utf-8', driverName='ESRI Shapefile', onlySelected=True)
    print(file_name)