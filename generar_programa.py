import os
import pandas as pd
import numpy as np
from pylatex import Document, Package, Command, PageStyle, Head, Foot, NewPage,\
    TextColor, MiniPage, StandAloneGraphic, simple_page_number,\
    TikZ, TikZNode, TikZOptions, TikZCoordinate, TikZNodeAnchor, TikZPath,\
    UnsafeCommand,\
    VerticalSpace, HorizontalSpace, NewLine,\
    LongTable
from pylatex.base_classes import Environment, Arguments
from pylatex.utils import NoEscape, bold, italic

class ExampleEnvironment(Environment):
    _latex_name = 'parcolumns'
    packages = [Package('parcolumns')]

def textcolor(size,vspace,color,bold,text,hspace="0",par=True):
    dump = NoEscape(r"")
    if par==True:
        dump = NoEscape(r"\par")
    if hspace!="0":
        dump += NoEscape(HorizontalSpace(hspace,star=True).dumps())
    dump += NoEscape(Command("fontsize",arguments=Arguments(size,vspace)).dumps())
    dump += NoEscape(Command("selectfont").dumps()) + NoEscape(" ")
    if bold==True:
        dump += NoEscape(Command("textbf", NoEscape(Command("textcolor",arguments=Arguments(color,text)).dumps())).dumps())
    else:
        dump += NoEscape(Command("textcolor",arguments=Arguments(color,text)).dumps())
    return dump

def number_to_ordinals(number_str):
    match number_str:
        case "1" | "3":
            number_str += r"\textsuperscript{er}"
        case "2":
            number_str += r"\textsuperscript{do}"
        case "4" | "5" | "6":
            number_str += r"\textsuperscript{to}"
        case "7" | "10":
            number_str += r"\textsuperscript{mo}"
        case "8":
            number_str += r"\textsuperscript{vo}"
        case "9":
            number_str += r"\textsuperscript{no}"
    return number_str 

cursos = pd.read_csv("cursos_IEM.csv")
datos_gen = pd.read_csv("datos_IEM.csv")
descrip_obj = pd.read_csv("descrip_obj_IEM.csv")


def generar_programa(codigo):

    codCurso = codigo
    nomEscue = "Escuela de Ingeniería Electromecánica"
    lisProgr = pd.DataFrame() 
    lisProgr = cursos[cursos.Codigo == codCurso].Programas.str.split(';',expand=True)
    lisProgr.reset_index(inplace = True, drop = True)
    lisProgrShape = lisProgr.shape[1]
    print(lisProgr)
    if lisProgrShape > 2:
        strProgr = "Carreras de: "
    else:
        strProgr = "Carrera de "
    for columna in range(int(lisProgrShape/2)):
        if columna == 0:
            strProgr += lisProgr[columna*2].item()
        else:
            strProgr += "; "
            strProgr += lisProgr[columna*2].item()
    nomCurso = cursos[cursos.Codigo == codCurso].Nombre.item()
    tipCurso = datos_gen[datos_gen.Codigo == codCurso].Tipo.item()
    eleCurso = datos_gen[datos_gen.Codigo == codCurso].Electivo.item()
    porAreas = datos_gen[datos_gen.Codigo == codCurso].AreasCurriculares.item()

    ubiLista = pd.DataFrame("", index=pd.RangeIndex(lisProgrShape/2), columns=["programa", "semestre"])# pd.DataFrame("", index=pd.RangeIndex(10), columns=pd.RangeIndex(10))
    
    for pos in range(int(lisProgrShape/2)):
        ubiLista.iloc[pos, ubiLista.columns.get_loc("programa")] = lisProgr[pos*2].item()
        ubiLista.iloc[pos, ubiLista.columns.get_loc("semestre")] = lisProgr[pos*2+1].item()
    print(ubiLista)
#Genera ubicación en el plan de estudios en las diferentes carreras
    ubiPlane = ""
    for sem in range(1,int(ubiLista["semestre"].max())+1):
        filter = ubiLista["semestre"] == str(sem)
        filterlist = ubiLista[filter]
        shape = filterlist.shape[0]
        if shape  != 0:
            ubiPlane += "Curso de "
            ubiPlane += number_to_ordinals(str(sem))
            ubiPlane += " semestre en "
            fila = 0
            for index, row in filterlist.iterrows():
                ubiPlane += row["programa"]
                fila += 1
                if fila == shape:
                    ubiPlane += ". "
                elif fila == shape - 1:
                    ubiPlane += " e "              
                else:
                    ubiPlane += "; "

    susRequi = datos_gen[datos_gen.Codigo == codCurso].Requisitos.item()
    corRequi = datos_gen[datos_gen.Codigo == codCurso].Correquisitos.item()
    essRequi = datos_gen[datos_gen.Codigo == codCurso].EsRequisito.item()
    tipAsist = datos_gen[datos_gen.Codigo == codCurso].Asistencia.item()
    posRecon = datos_gen[datos_gen.Codigo == codCurso].PosibilidadReconocimiento.item()
    posSufic = datos_gen[datos_gen.Codigo == codCurso].PosibilidadSuficiencia.item()
    numCredi = datos_gen[datos_gen.Codigo == codCurso].Creditos.item()
    horClass = datos_gen[datos_gen.Codigo == codCurso].HorasClase.item()
    horExtra = datos_gen[datos_gen.Codigo == codCurso].HorasExtraclase.item()
    vigProgr = datos_gen[datos_gen.Codigo == codCurso].Vigencia.item()
    desGener = descrip_obj[descrip_obj.Codigo == codCurso].Descripcion.item()
    objGener = descrip_obj[descrip_obj.Codigo == codCurso].ObjetivoGeneral.item()
    objEspec = descrip_obj[descrip_obj.Codigo == codCurso].ObjetivosEspecificos.item()
    conCurso = descrip_obj[descrip_obj.Codigo == codCurso].Contenidos.item()
    nomProfe = "Juan José Rojas Hernández"
    corProfe = "juan.rojas@itcr.ac.cr"
    conProfe = "Miercoles 7:30 a.m. - 10: 30 a.m." #Esto seria mejor construirlo tambien 
    #Geometry
    geometry_options = { 
        "left": "22.5mm",
        "right": "16.1mm",
        "top": "48mm",
        "bottom": "25mm",
        "headheight": "12.5mm",
        "footskip": "12.5mm"
    }
    #Document options
    doc = Document(documentclass="article", \
                   fontenc=None, \
                   inputenc=None, \
                   lmodern=False, \
                   textcomp=False, \
                   page_numbers=True, \
                   indent=False, \
                   document_options=["letterpaper"],
                   geometry_options=geometry_options)
    #Packages
    doc.packages.append(Package(name="fontspec", options=None))
    doc.packages.append(Package(name="babel", options=['spanish',"activeacute"]))
    doc.packages.append(Package(name="graphicx"))
    doc.packages.append(Package(name="tikz"))
    doc.packages.append(Package(name="anyfontsize"))
    doc.packages.append(Package(name="xcolor"))
    doc.packages.append(Package(name="colortbl"))
    doc.packages.append(Package(name="array"))
    doc.packages.append(Package(name="float"))
    #doc.packages.append(Package(name="lastpage")) con pagenumbers+true
    doc.packages.append(Package(name="longtable"))
    doc.packages.append(Package(name="multirow"))
    doc.packages.append(Package(name="fancyhdr"))
    #Package options
    doc.preamble.append(Command('setmainfont','Arial'))
    doc.preamble.append(Command('usetikzlibrary','calc'))
    doc.add_color('gris','rgb','0.27,0.27,0.27') #70,70,70
    doc.add_color('parte','rgb','0.02,0.204,0.404') #5,52,103
    doc.add_color('azulsuaveTEC','rgb','0.02,0.455,0.773') #5,116,197
    doc.add_color('fila','rgb','0.929,0.929,0.929') #237,237,237
    doc.add_color('linea','rgb','0.749,0.749,0.749') #191,191,191

    headerfooter = PageStyle("headfoot")

    #Left header
    with headerfooter.create(Head("L")) as header_left:
        with header_left.create(MiniPage(width=r"0.5\textwidth",align="l")) as logobox:
            logobox.append(StandAloneGraphic(image_options="width=62.5mm", filename='../figuras/Logo.png'))
    #Left foot
    with headerfooter.create(Foot("L")) as footer_left:
        footer_left.append(TextColor("azulsuaveTEC", f"{nomEscue}"))
        footer_left.append(NoEscape(r"\par \parbox{0.85\textwidth}{"))
        footer_left.append(textcolor
            (   
            par=False,
            size="8",
            vspace="0",
            color="azulsuaveTEC",
            bold=False,
            text=f"{strProgr}" 
            ))
        footer_left.append(NoEscape(r"}"))
    #Right foot
    with headerfooter.create(Foot("R")) as footer_right:
        footer_right.append(TextColor("azulsuaveTEC", NoEscape(r"Página \thepage \hspace{1pt} de \pageref{LastPage}")))        
  
    title = NoEscape(
    r'''
    \vspace*{170mm}

    \fontsize{14}{0}\selectfont Programa del curso \codCurso

    \fontsize{18}{25}\selectfont \textbf{\textcolor{azulsuaveTEC}{\nomCurso}}

    \hspace*{10mm}\fontsize{12}{40}\selectfont \color{black!40!gray}\nomEscue

    \hspace*{10mm}\fontsize{12}{14}\selectfont \color{black!40!gray}\nomProgr
    '''
    )

    doc.preamble.append(headerfooter)
    doc.change_page_style("empty")
    with doc.create(TikZ(
            options=TikZOptions
                (    
                "overlay",
                "remember picture"
                )
        )) as logo:
        logo.append(TikZNode(\
            options=TikZOptions
                (
                "inner sep = 0mm",
                "outer sep = 0mm",
                "anchor = north west",
                "xshift = -23mm",
                "yshift = 22mm"
                ),
            text=StandAloneGraphic(image_options="width=21cm", filename='../figuras/Logo_portada.png').dumps(),\
            at=TikZCoordinate(0,0)
        ))
    doc.append(VerticalSpace("150mm", star=True))
    doc.append(textcolor
            (   
            size="14",
            vspace="0",
            color="black",
            bold=False,
            text=f"Programa del curso {codCurso}" 
            ))
    doc.append(textcolor
            (  
            size="18",
            vspace="25",
            color="azulsuaveTEC",
            bold=True,
            text=f"{nomCurso}" 
            ))
    with doc.create(LongTable(table_spec=r"m{0.02\textwidth}m{0.98\textwidth}",row_height=0.7)) as table:
            table.add_row(["", textcolor
            (   
            par=False,
            hspace="0mm",
            size="12",
            vspace="14",
            color="gris",
            bold=True,
            text=f"{nomEscue}"
            )])
            table.add_row(["", textcolor
            (   
            par=False,
            hspace="0mm",
            size="12",
            vspace="14",
            color="gris",
            bold=True,
            text=f"{strProgr}" 
            )])
    doc.append(NewPage())
    doc.change_document_style("headfoot")
    doc.append(textcolor
            (   
            size="14",
            vspace="0",
            color="parte",
            bold=True,
            text="I parte: Aspectos relativos al plan de estudios"
            ))
    doc.append(textcolor
            (   
            hspace="4mm",
            size="12",
            vspace="20",
            color="parte",
            bold=True,
            text="1 Datos generales"
            ))
    with doc.create(LongTable(table_spec=r"m{7cm}m{9cm}",row_height=1.5)) as table:
            table.add_row([bold("Nombre del curso:"), f"{nomCurso}"])
            table.add_row([bold("Código:"), f"{codCurso}"])
            table.add_row([bold("Tipo de curso:"), f"{tipCurso}"])
            table.add_row([bold("Electivo o no:"), f"{eleCurso}"])
            table.add_row([bold("Nº de créditos:"), f"{numCredi}"])
            table.add_row([bold("Nº horas de clase por semana:"), f"{horClass}"])
            table.add_row([bold("Nº horas extraclase por semana:"), f"{horExtra}"])
            table.add_row([bold("% de areas curriculares:"), f"{porAreas}"])
            table.add_row([bold("Ubicación en el plan de estudios:"), NoEscape(f"{ubiPlane}")])
            table.add_row([bold("Requisitos:"), f"{susRequi}"])
            table.add_row([bold("Correquisitos:"), f"{corRequi}"])
            table.add_row([bold("El curso es requisito de:"), f"{essRequi}"])
            table.add_row([bold("Asistencia:"), f"{tipAsist}"])
            table.add_row([bold("Suficiencia:"), f"{posSufic}"])
            table.add_row([bold("Posibilidad de reconocimiento:"), f"{posRecon}"])
            table.add_row([bold("Vigencia del programa:"), f"{vigProgr}"])
    doc.append(NewPage())
    with doc.create(LongTable(table_spec=r"p{0.18\textwidth}p{0.72\textwidth}")) as table:
            table.add_row([
                textcolor
                    (
                    size="12",
                    vspace="0",
                    color="parte",
                    bold=True,
                    text="2 Descripción general"
                    ),
                    f"{desGener}"
                ])
            table.add_row([
                textcolor
                    (
                    size="12",
                    vspace="0",
                    color="parte",
                    bold=True,
                    text="3 Objetivos"
                    ),
                    f"{objGener}"
                ])
            table.add_row([
                "",
                f"{objEspec}"
                ])
            table.add_row([
                textcolor
                    (
                    size="12",
                    vspace="0",
                    color="parte",
                    bold=True,
                    text="4 Contenidos"
                    ),
                    f"{conCurso}"
                ])
    doc.append(textcolor
    (   
    size="14",
    vspace="0",
    color="parte",
    bold=True,
    text="II parte: Aspectos operativos"
    ))
    doc.generate_pdf(f"./programas/{codCurso}", clean=True, clean_tex=False, compiler='lualatex')

# for codigo in cursos.Codigo:
#      generar_programa(codigo)
    
generar_programa("IEM2301")