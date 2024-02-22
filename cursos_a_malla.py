import pandas as pd


cursos = pd.read_csv("cursos_EM.csv")
cursos_malla = pd.read_csv("malla_EM.csv")

cursos_malla.HorasTeoria = cursos_malla.HorasTeoria.astype(int)
cursos_malla.HorasPractica = cursos_malla.HorasPractica.astype(int)
cursos_malla.Creditos = cursos_malla.Creditos.astype(int)

for codigo in cursos.Codigo:
    cursos_malla.loc[cursos_malla.Codigo == codigo, 'Nombre'] = cursos[cursos.Codigo == codigo].Nombre.item()
    cursos_malla.loc[cursos_malla.Codigo == codigo, 'Area'] = cursos[cursos.Codigo == codigo].Area.item()
    cursos_malla.loc[cursos_malla.Codigo == codigo, 'HorasTeoria'] = cursos[cursos.Codigo == codigo].HorasTeoria.item()
    cursos_malla.loc[cursos_malla.Codigo == codigo, 'HorasPractica'] = round(cursos[cursos.Codigo == codigo].HorasPractica.item())
    cursos_malla.loc[cursos_malla.Codigo == codigo, 'Creditos'] = cursos[cursos.Codigo == codigo].Creditos.item()

print(cursos_malla.dtypes)
cursos_malla.to_csv('malla_EM.csv', index=False, encoding='utf-8-sig')

# print(cursos.head(30))
# print(cursos_malla.head(30))