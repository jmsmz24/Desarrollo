import arcpy

arcpy.env.workspace = r"C:\DesarrolloRepo\Arcpy\TemplateData.gdb\World"
featureclasses = arcpy.ListFeatureClasses()

for fc in featureclasses:
    desc = arcpy.Describe(fc)
    print(fc + " - " + desc.shapeType + " - Z:" + str(desc.hasZ) + " - M:" + str(desc.hasM))