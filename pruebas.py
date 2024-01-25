import pandas as pd

cursos = pd.read_csv("cursos.csv")
print(cursos.head())
datos_gen = pd.read_csv("datos_gen.csv")
print(datos_gen.head())