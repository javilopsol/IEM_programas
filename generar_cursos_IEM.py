import pandas as pd

cursos_IE = pd.read_csv("cursos_IE.csv")
cursos_mante = pd.read_csv("cursos.csv")
cursos_IA = pd.read_csv("aeronauticaV2.csv")

cursos=pd.DataFrame()
cursos["Codigo"]=pd.concat([cursos_mante.loc[:,"Codigo"], cursos_IE.loc[:,"Codigo"]], ignore_index=True)
cursos["Nombre"]=pd.concat([cursos_mante.loc[:,"Nombre"], cursos_IE.loc[:,"Nombre"]], ignore_index=True)

contador=0

for curso in cursos_IA.loc[:,"Codigo"]:
    codigo=curso
    codigoIA=codigo[:4]

    if codigoIA=="IE25":

        contador=contador+1

    else:
        contador=contador+1

cursos.to_csv('cursos_IEM.csv', index=False,encoding='utf-8-sig' )