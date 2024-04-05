import pandas as pd
import numpy as np

cursos = pd.read_csv("cursos_IEM.csv")
mante = pd.read_csv("mantenimiento.csv")
elect = pd.read_csv("electromecanica.csv")
aer1 = pd.read_csv("aeronauticaV1.csv")
aer2 = pd.read_csv("aeronauticaV2.csv")

## cursos.HorasTeoria = cursos_malla.HorasTeoria.astype(int)
# # cursos_malla.HorasPractica = cursos_malla.HorasPractica.astype(int)
# # cursos_malla.Creditos = cursos_malla.Creditos.astype(int)

mallas = pd.concat([mante,elect,aer1,aer2])
mallas.reset_index(inplace = True, drop = True)
#newmallas = mallas.merge(aer1, how='outer', on='Programa')
print(mallas)


for codigo in cursos.Codigo:
    mallas.loc[mallas.Codigo == codigo, 'Nombre'] = cursos[cursos.Codigo == codigo].Nombre.item()
    # malla.loc[malla.Codigo == codigo, 'Area'] = cursos[cursos.Codigo == codigo].Area.item()
    # malla.loc[malla.Codigo == codigo, 'HorasTeoria'] = cursos[cursos.Codigo == codigo].HorasTeoria.item()
    # malla.loc[malla.Codigo == codigo, 'HorasPractica'] = round(cursos[cursos.Codigo == codigo].HorasPractica.item())
    # malla.loc[malla.Codigo == codigo, 'Creditos'] = cursos[cursos.Codigo == codigo].Creditos.item()

# # for codigo in cursos2.Codigo:
# #     print(codigo)
# #     print(cursos2[cursos2.Codigo == codigo].Nombre.item())
# #     malla.loc[malla.Codigo == codigo, 'Nombre'] = cursos2[cursos2.Codigo == codigo].Nombre.item()
# #     #malla.loc[malla.Codigo == codigo, 'Programa'] = 'AeronáuticaV2'
# print(aer1)
# print(mallaold)
# print(malla)
mallas.to_csv('mallas_IEM.csv', index=False, encoding='utf-8-sig')