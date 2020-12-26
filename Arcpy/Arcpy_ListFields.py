import arcpy

arcpy.env.workspace = r"C:\DesarrolloRepo\Arcpy\TemplateData.gdb\World"
featureclasses = arcpy.ListFeatureClasses()

for fc in featureclasses:
    fields = arcpy.ListFields(fc)
    for field in fields:
        name = field.name
        type = field.type
        length = field.length
        print(fc+" -> "+name+" - "+type+" - "+str(length))