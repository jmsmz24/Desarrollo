#Ej1 - Calcula el resumen de estadísticas agrupadas para los campos en una capa

# Función calcula el sumatorio. Parametr

def summarize (layer, a, b):
    
    features = layer.getFeatures()
    suma_total = {} 

    for feature in features:
        campo_agrupacion = feature[a]
        campo_estadistica = feature[b]

        if campo_estadistica > 0:
            if campo_agrupacion in suma_total:
                suma_total[campo_agrupacion] += campo_estadistica
            else:
                suma_total[campo_agrupacion] = campo_estadistica

    print (suma_total)
    
layer = iface.activeLayer()
summarize (layer,"NAME_1","area")

