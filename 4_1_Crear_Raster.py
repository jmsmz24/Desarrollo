from osgeo import gdal, osr
import numpy as np
 
fn = 'C:\\ISM_PyQGIS\\raster.tif'
 
rasterband = np.zeros((10,10))
 
driver = gdal.GetDriverByName('GTiff')
ds = driver.Create(fn, xsize=10, ysize=10, bands=1, eType=gdal.GDT_Float32)
ds.GetRasterBand(1).WriteArray(rasterband)
 
extent = [-4.164151647999999, 10, 0, 40.5162820019999970, 0, 10]
ds.SetGeoTransform(extent)
srs = osr.SpatialReference()
srs.SetWellKnownGeogCS('WGS84')
ds.SetProjection(srs.ExportToWkt())
ds = None
 
rlayer = iface.addRasterLayer(fn)
