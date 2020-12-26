
def hemisphere(geom):
	box = geom.boundingBox()
	if box.yMinimum() > 0 and box.yMaximum() > 0:
		return "N"
	if box.yMinimum() <= 0 and box.yMaximum() <= 0:
		return "S"
	else:
		return "A"

layer = iface.activeLayer()
features = layer.getFeatures()

for feat in features:
	geom = feat.geometry()            
	hemi = hemisphere(geom)
	print(hemi)