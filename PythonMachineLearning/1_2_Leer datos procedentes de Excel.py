import pandas as pd
import os

mainpath = "C:\DesarrolloRepo\PythonMachineLearning\datasets"
filename = "covid19_tia_zonas_basicas_salud_s.xlsx"
fullpath = os.path.join(mainpath,filename)

df = pd.read_excel(fullpath,"covid")

list= ["zona","fecha","incidencia_acumulada14"]

df2 = pd.DataFrame(columns=list)
print(df2)

for index, row in df.iterrows():
    print(row['zona_basica_salud'],row['fecha_informe'],row['tasa_incidencia_acumulada_ultimos_14dias'])

#df.to_excel(mainpath+"/zona.xlsx")