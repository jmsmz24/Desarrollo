#UD3. Introducción a programación en QGIS3
#3.4. Creando capas de puntos, línea y polígono
#3.4.1.Crear Capa Raster
####################################################################################################


from osgeo import gdal, osr
import numpy

path = 'C:\\ISM_PyQGIS\\raster.tif'

#Crearemos una variable que representa una matriz bidimensional con 10 filas y 10 columnas. La matriz 2D se rellenará con ceros.
rasterband = numpy.zeros((10,10))

#Recuperar el controlador geotiff y crear un nuevo ráster de 10 filas, 10 columnas, 1 banda float de 32 bits
driver = gdal.GetDriverByName('GTiff')
ds = driver.Create(fn, xsize=10, ysize=10, bands=1, eType=gdal.GDT_Float32)

#Escribir en banda 1 del ráster los datos de la matriz rasterband (siempre y cuando coincida con las dimensiones en ambas)
ds.GetRasterBand(1).WriteArray(rasterband)

#Añadir una referencia espacial (1). Geotransformación,proporciona las coordenadas parte superior izquierda del raster
geotransformation = [441781.256, 10, 0, 4473184.962, 0, -10]
ds.SetGeoTransform(geotransformation)

#Añadir una referencia espacial (2). Referencia espacial y proyección.
srs = osr.SpatialReference()
srs.SetUTM(30,1)
srs.SetWellKnownGeogCS('ETRS89')
ds.SetProjection(srs.ExportToWkt())

#Cerrar  raster y agregar a la interfaz QGIS.
ds = None
rlayer = iface.addRasterLayer(path)
