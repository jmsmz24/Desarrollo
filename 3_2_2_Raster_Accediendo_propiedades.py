#UD3. Introducción a programación en QGIS3
#3.2. Creando capas de puntos, línea y polígono
#3.2.2. Raster: Accediendo campos entidades geometrías
####################################################################################################

#Accedemos a la capa raster actualmente activa en QGIS, 
raster = iface.activeLayer()

#Nombre de la capa en QGIS: 
raster.name()

#Extent de la capa: 
raster.extent()

#Sistema de coordenadas: 
raster.crs()

#Dimensiones del ráster en pixeles:
raster.width()
raster.height()

#Número de bandas: 
raster.bandCount()

#Tipo de raster: 
raster.rasterType() 

#Metadatos
raster.metadata()

#Acceso a estadisticas con objeto de tipo QgsRasterDataProvider y los guardamos en una variable llamada provider. 
provider = raster.dataProvider()
stats = provider.bandStatistics(1, QgsRasterBandStats.All)

#Acceso a estadísticas utilizando la variable stats.
stats.minimumValue
stats.minimumValue
stats.mean
stats.range
stats.stdDev
stats.sum
stats.sumOfSquares



