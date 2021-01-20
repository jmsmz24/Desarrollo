import pandas as pd
import matplotlib.pyplot
import tkinter
from tkinter import *

url= "https://datos.comunidad.madrid/catalogo/dataset/b3d55e40-8263-4c0b-827d-2bb23b5e7bab/resource/43708c23-2b77-48fd-9986-fa97691a2d59/download/covid19_tia_zonas_basicas_salud_s.csv"

df = pd.read_csv(url,";", encoding='latin-1')
print(df.head())

df.plot(kind="scatter", x="casos_confirmados_activos_ultimos_14dias", y="casos_confirmados_ultimos_14dias")