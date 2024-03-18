import pandas as pd

cursos = pd.read_csv("cursos_IEM.csv")
datos_gen = pd.read_csv("datos_IEM.csv")
descrip_obj = pd.read_csv("descrip_obj_IEM.csv")

codigo = "IEM2301"
codCurso = codigo
lisProgr = cursos[cursos.Codigo == codCurso].Programas.str.split('\n',expand=False).explode()
lisProgr = lisProgr.str.split(';',expand=True)
lisProgr.reset_index(inplace = True, drop = True)
lisProgr.columns = ['programa','semestre']


if len(lisProgr) > 1:
    strProgr = "Carreras de: " + ' e'.join(lisProgr['programa'].str.cat(sep='; ').rsplit(';',1))
else:
    strProgr = "Carrera de " + lisProgr['programa'].item()


contenidos = pd.DataFrame()
contenidos = descrip_obj[descrip_obj.Codigo == codCurso].Contenidos.str.split('\r\n',expand=False).explode()
contenidos.reset_index(inplace = True, drop = True)
nivel_1, nivel_2, nivel_3 = [0,0,0]
for index, row in contenidos.items():
    res = 0
    for pos in range(3):
        if pos == row.find('*', pos, pos+1):
            res += 1
    if res == 1:
        nivel_1 += 1
        nivel_2 = 0
        contenidos.iloc[index] = row.replace('*', f"{str(nivel_1)} ")
    elif res == 2:
        nivel_2 += 1
        nivel_3 = 0
        contenidos.iloc[index] = row.replace('**', f"  {str(nivel_1)}.{str(nivel_2)} ")
    elif res == 3:
        nivel_3 += 1
        contenidos.iloc[index] = row.replace('***', f"    {str(nivel_1)}.{str(nivel_2)}.{str(nivel_3)} ")

objGener = descrip_obj[descrip_obj.Codigo == codCurso].ObjetivoGeneral.item()

objEspec = descrip_obj[descrip_obj.Codigo == codCurso].ObjetivosEspecificos.str.split('\n',expand=False).explode()
objEspec.reset_index(inplace = True, drop = True)
print(objEspec)



