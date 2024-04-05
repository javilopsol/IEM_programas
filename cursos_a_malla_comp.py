import pandas as pd
import numpy as np

cursos = pd.read_csv("cursos_IEM.csv")
mante = pd.read_csv("mantenimiento.csv")
elect = pd.read_csv("electromecanica.csv")
aer1 = pd.read_csv("aeronauticaV1.csv")
aer2 = pd.read_csv("aeronauticaV2.csv")

mallas = pd.concat([mante,elect,aer1,aer2])
mallas.reset_index(inplace = True, drop = True)

mallas['Compartido'] = ""

mallascomp = mallas.loc[(mallas.Programa == "AeronáuticaV2") | (mallas.Programa == "Electromecánica")]

counts = mallascomp.Codigo.value_counts()

for codigo in mallascomp.Codigo:
    if counts[counts.index == codigo].item() > 1:
        mallascomp.loc[mallascomp.Codigo == codigo, 'Compartido'] = "SI"
    else:
        mallascomp.loc[mallascomp.Codigo == codigo, 'Compartido'] = "NO"

mallascomp.to_csv('mallas_IEM_comp.csv', index=False, encoding='utf-8-sig')