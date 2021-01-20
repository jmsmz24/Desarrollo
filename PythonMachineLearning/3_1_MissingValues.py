import pandas as pd

url= "https://datos.comunidad.madrid/catalogo/dataset/b3d55e40-8263-4c0b-827d-2bb23b5e7bab/resource/43708c23-2b77-48fd-9986-fa97691a2d59/download/covid19_tia_zonas_basicas_salud_s.csv"

df = pd.read_csv(url,";", encoding='latin-1')

#print(df.notnull().sum())
#print(df.isnull().sum())

#Borrado valores que falta
df2=df
df2.dropna(axis=0, how="any")#Borra filas con valores vacios
#print(df2.isnull().sum())

df3=df
df3.fillna(0)

for index, row in df3.iterrows():
    print(row['zona_basica_salud'],row['fecha_informe'],row['tasa_incidencia_acumulada_ultimos_14dias'])

