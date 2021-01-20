import pandas as pd

url= "https://datos.comunidad.madrid/catalogo/dataset/b3d55e40-8263-4c0b-827d-2bb23b5e7bab/resource/43708c23-2b77-48fd-9986-fa97691a2d59/download/covid19_tia_zonas_basicas_salud_s.csv"

df = pd.read_csv(url,";", encoding='latin-1')

print(df.head(10))#primeros 10 valores
print(df.shape)#dimensiones
print(df.dtypes)##tipo de columnas
print(df.describe())#Estadisticos básicos campos numericos
