#UD3. Introducción a programación en QGIS3
#3.2. Creando capas de puntos, línea y polígono
#3.2.2. Raster: Accediendo campos entidades geometrías
####################################################################################################

#Accedemos a la capa raster actualmente activa en QGIS, 
raster = iface.activeLayer()

#Nombre de la capa en QGIS: 
print(raster.name())

#Extent de la capa: 
print(raster.extent())

#Sistema de coordenadas: 
print(raster.crs())

#Dimensiones del ráster en pixeles:
print(raster.width())
print(raster.height())

#Número de bandas: 
print(raster.bandCount())

#Tipo de raster: 
print(raster.rasterType()) 

#Metadatos
print(raster.metadata())

#Acceso a estadisticas con objeto de tipo QgsRasterDataProvider y los guardamos en una variable llamada provider. 
provider = raster.dataProvider()
stats = provider.bandStatistics(1, QgsRasterBandStats.All)

#Acceso a estadísticas utilizando la variable stats.
print(stats.minimumValue)
print(stats.minimumValue)
print(stats.mean)
print(stats.range)
print(stats.stdDev)
print(stats.sum)
print(stats.sumOfSquares)



