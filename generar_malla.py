import os
import pandas as pd
from pylatex import Document, Package, Command, PageStyle, Head, Foot, NewPage,\
    TextColor, MiniPage, StandAloneGraphic, simple_page_number,\
    TikZ, TikZScope, TikZNode, TikZOptions, TikZCoordinate, TikZNodeAnchor, TikZPath,\
    UnsafeCommand,\
    VerticalSpace, HorizontalSpace, NewLine,\
    LongTable
from pylatex.base_classes import Environment, Arguments
from pylatex.utils import NoEscape, bold, italic

cursos = pd.read_csv("malla_EM.csv")
print(cursos.head())

def textcolor(size,vspace,color,bold,text,hspace="0"):
    dump = NoEscape(r"\par")
    if hspace!="0":
        dump += NoEscape(HorizontalSpace(hspace,star=True).dumps())
    dump += NoEscape(Command("fontsize",arguments=Arguments(size,vspace)).dumps())
    dump += NoEscape(Command("selectfont").dumps()) + NoEscape(" ")
    if bold==True:
        dump += NoEscape(Command("textbf", NoEscape(Command("textcolor",arguments=Arguments(color,text)).dumps())).dumps())
    else:
        dump += NoEscape(Command("textcolor",arguments=Arguments(color,text)).dumps())
    #dump += NoEscape("\par")
    return dump

def colocar_curso(codCurso,columna,semestre):
    dump = NoEscape(f"\draw ({5*columna},{4*semestre})")
    dump += NoEscape("pic{curso={MA0101,Matemática General,5,0,2,lime}};")
    return dump


def generar_malla(programa):
    # codCurso = codigo
    # nomEscue = "Escuela de Ingeniería Electromecánica"
    # nomProgr = cursos[cursos.Codigo == codCurso].Programa.item()
    # nomCurso = cursos[cursos.Codigo == codCurso].Nombre.item()
    # tipCurso = datos_gen[datos_gen.Codigo == codCurso].Tipo.item()
    # eleCurso = datos_gen[datos_gen.Codigo == codCurso].Electivo.item()
    # porAreas = datos_gen[datos_gen.Codigo == codCurso].AreasCurriculares.item()
    # ubiPlane = datos_gen[datos_gen.Codigo == codCurso].Ubicacion.item()
    # susRequi = datos_gen[datos_gen.Codigo == codCurso].Requisitos.item()
    # corRequi = datos_gen[datos_gen.Codigo == codCurso].Correquisitos.item()
    # essRequi = datos_gen[datos_gen.Codigo == codCurso].EsRequisito.item()
    # tipAsist = datos_gen[datos_gen.Codigo == codCurso].Asistencia.item()
    # posRecon = datos_gen[datos_gen.Codigo == codCurso].PosibilidadReconocimiento.item()
    # posSufic = datos_gen[datos_gen.Codigo == codCurso].PosibilidadSuficiencia.item()
    # numCredi = datos_gen[datos_gen.Codigo == codCurso].Creditos.item()
    # horClass = datos_gen[datos_gen.Codigo == codCurso].HorasClase.item()
    # horExtra = datos_gen[datos_gen.Codigo == codCurso].HorasExtraclase.item()
    # vigProgr = datos_gen[datos_gen.Codigo == codCurso].Vigencia.item()
    # desGener = descrip_obj[descrip_obj.Codigo == codCurso].Descripcion.item()
    # objGener = descrip_obj[descrip_obj.Codigo == codCurso].ObjetivoGeneral.item()
    # objEspec = descrip_obj[descrip_obj.Codigo == codCurso].ObjetivosEspecificos.item()

    # nomProfe = "Juan José Rojas Hernández"
    # corProfe = "juan.rojas@itcr.ac.cr"
    # conProfe = "Miercoles 7:30 a.m. - 10: 30 a.m." #Esto seria mejor construirlo tambien 

    #Geometry
    geometry_options = { 
        "left": "0mm",
        "right": "0mm",
        "top": "0mm",
        "bottom": "0mm",
        "headheight": "1mm",
        "footskip": "1mm"
    }
    #Document options
    doc = Document(documentclass="article", \
                   fontenc=None, \
                   inputenc=None, \
                   lmodern=False, \
                   textcomp=False, \
                   page_numbers=True, \
                   indent=False, \
                   document_options=["letterpaper","lanscape"],
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
    #Prueba
    bloqueCurso = NoEscape(
    r'''\tikzset{
            pics/curso/.style args={#1,#2,#3,#4,#5,#6}{
            code={
                \def\ancho{4}
                \def\alto{0.7}
                \draw[fill=#6] (-\ancho/2,\alto) rectangle (\ancho/2,-\alto) node[midway,align=center,text width=4cm]{\fontsize{10pt}{12pt}\selectfont \textbf{#2}};
                \draw[fill=#6] (-\ancho/2,\alto) rectangle (\ancho/2,\alto + \alto) node[midway]{\fontsize{12pt}{14pt}\selectfont #1};
                \draw[fill=#6] (-\ancho/2,-\alto) rectangle (-\ancho/2 + \ancho/3, -\alto - \alto) node[midway]{\fontsize{12pt}{14pt}\selectfont #3};
                \draw[fill=#6] (-\ancho/2 + \ancho/3,-\alto) rectangle (-\ancho/2 + 2*\ancho/3, -\alto - \alto) node[midway]{\fontsize{12pt}{14pt}\selectfont #4};
                \draw[fill=#6] (-\ancho/2 + 2*\ancho/3,-\alto) rectangle (-\ancho/2 + 3*\ancho/3, -\alto - \alto) node[midway]{\fontsize{12pt}{14pt}\selectfont #5};
            }
        }
    }'''
    )

        
    doc.preamble.append(bloqueCurso)
    
    with doc.create(TikZ(
            options=TikZOptions
                (    
                "scale = 0.5",
                "transform shape"
                )
        )) as malla:
        malla.append(colocar_curso("MA0101",1,1))
        malla.append(colocar_curso("MA0101",1,2))
        malla.append(colocar_curso("MA0101",2,1))



    # # #Variables
    # # doc.set_variable("nomEscue",nomEscue)
    # # doc.set_variable("nomProgr",nomProgr)
    # # doc.set_variable("codCurso",codCurso)
    # # doc.set_variable("nomCurso",nomCurso)
    # # doc.set_variable("tipCurso",tipCurso)
    # # doc.set_variable("eleCurso",eleCurso)
    # # doc.set_variable("porAreas",porAreas)
    # # doc.set_variable("ubiPlane",ubiPlane)
    # # doc.set_variable("susRequi",susRequi)
    # # doc.set_variable("corRequi",corRequi)
    # # doc.set_variable("essRequi",essRequi)
    # # doc.set_variable("tipAsist",tipAsist)
    # # doc.set_variable("posRecon",posRecon)
    # # doc.set_variable("posSufic",posSufic)
    # # doc.set_variable("numCredi",numCredi)
    # # doc.set_variable("horClass",horClass)
    # # doc.set_variable("horExtra",horExtra)
    # # doc.set_variable("vigProgr",vigProgr)
    # # doc.set_variable("nomProfe",nomProfe)
    # # doc.set_variable("corProfe",corProfe)
    # # doc.set_variable("conProfe",conProfe)
    # #Package options
    # doc.preamble.append(Command('setmainfont','Arial'))
    # doc.preamble.append(Command('usetikzlibrary','calc'))
    # doc.add_color('gris','rgb','0.27,0.27,0.27') #70,70,70
    # doc.add_color('parte','rgb','0.02,0.204,0.404') #5,52,103
    # doc.add_color('azulsuaveTEC','rgb','0.02,0.455,0.773') #5,116,197
    # doc.add_color('fila','rgb','0.929,0.929,0.929') #237,237,237
    # doc.add_color('linea','rgb','0.749,0.749,0.749') #191,191,191

    # headerfooter = PageStyle("headfoot")

    # #Left header
    # with headerfooter.create(Head("L")) as header_left:
    #     with header_left.create(MiniPage(width=r"0.5\textwidth",align="l")) as logobox:
    #         logobox.append(StandAloneGraphic(image_options="width=62.5mm", filename='../figuras/Logo.png'))
    # #Left foot
    # with headerfooter.create(Foot("L")) as footer_left:
    #     footer_left.append(TextColor("azulsuaveTEC", f"{nomEscue} - {nomProgr}"))
    # #Right foot
    # with headerfooter.create(Foot("R")) as footer_right:
    #     footer_right.append(TextColor("azulsuaveTEC", NoEscape(r"Página \thepage \hspace{1pt} de \pageref{LastPage}")))        
  
    # title = NoEscape(
    # r'''
    # \vspace*{170mm}

    # \fontsize{14}{0}\selectfont Programa del curso \codCurso

    # \fontsize{18}{25}\selectfont \textbf{\textcolor{azulsuaveTEC}{\nomCurso}}

    # \hspace*{10mm}\fontsize{12}{40}\selectfont \color{black!40!gray}\nomEscue

    # \hspace*{10mm}\fontsize{12}{14}\selectfont \color{black!40!gray}\nomProgr
    # '''
    # )

    # doc.preamble.append(headerfooter)
    # doc.change_page_style("empty")
    # with doc.create(TikZ(
    #         options=TikZOptions
    #             (    
    #             "overlay",
    #             "remember picture"
    #             )
    #     )) as logo:
    #     logo.append(TikZNode(\
    #         options=TikZOptions
    #             (
    #             "inner sep = 0mm",
    #             "outer sep = 0mm",
    #             "anchor = north west",
    #             "xshift = -23mm",
    #             "yshift = 22mm"
    #             ),
    #         text=StandAloneGraphic(image_options="width=21cm", filename='../figuras/Logo_portada.png').dumps(),\
    #         at=TikZCoordinate(0,0)
    #     ))
    # doc.append(VerticalSpace("150mm", star=True))
    # doc.append(textcolor
    #         (   
    #         size="14",
    #         vspace="0",
    #         color="black",
    #         bold=False,
    #         text=f"Programa del curso {codCurso}" 
    #         ))
    # doc.append(textcolor
    #         (  
    #         size="18",
    #         vspace="25",
    #         color="azulsuaveTEC",
    #         bold=True,
    #         text=f"{nomCurso}" 
    #         ))
    # doc.append(textcolor
    #         (
    #         hspace="10mm",   
    #         size="12",
    #         vspace="30",
    #         color="gris",
    #         bold=True,
    #         text=f"{nomEscue}" 
    #         ))
    # doc.append(textcolor
    #         (   
    #         hspace="10mm",
    #         size="12",
    #         vspace="14",
    #         color="gris",
    #         bold=True,
    #         text=f"{nomProgr}" 
    #         ))
    # doc.append(NewPage())
    # doc.change_document_style("headfoot")
    # doc.append(textcolor
    #         (   
    #         size="14",
    #         vspace="0",
    #         color="parte",
    #         bold=True,
    #         text="I parte: Aspectos relativos al plan de estudios"
    #         ))
    # doc.append(textcolor
    #         (   
    #         hspace="4mm",
    #         size="12",
    #         vspace="20",
    #         color="parte",
    #         bold=True,
    #         text="1 Datos generales"
    #         ))
    # with doc.create(LongTable(table_spec=r"m{7cm}m{9cm}",row_height=1.5)) as table:
    #         table.add_row([bold("Nombre del curso:"), f"{nomCurso}"])
    #         table.add_row([bold("Código:"), f"{codCurso}"])
    #         table.add_row([bold("Tipo de curso:"), f"{tipCurso}"])
    #         table.add_row([bold("Electivo o no:"), f"{eleCurso}"])
    #         table.add_row([bold("Nº de créditos:"), f"{numCredi}"])
    #         table.add_row([bold("Nº horas de clase por semana:"), f"{horClass}"])
    #         table.add_row([bold("Nº horas extraclase por semana:"), f"{horExtra}"])
    #         table.add_row([bold("% de areas curriculares:"), f"{porAreas}"])
    #         table.add_row([bold("Ubicación en el plan de estudios:"), f"{ubiPlane}"])
    #         table.add_row([bold("Requisitos:"), f"{susRequi}"])
    #         table.add_row([bold("Correquisitos:"), f"{corRequi}"])
    #         table.add_row([bold("El curso es requisito de:"), f"{essRequi}"])
    #         table.add_row([bold("Asistencia:"), f"{tipAsist}"])
    #         table.add_row([bold("Suficiencia:"), f"{posSufic}"])
    #         table.add_row([bold("Posibilidad de reconocimiento:"), f"{posRecon}"])
    #         table.add_row([bold("Vigencia del programa:"), f"{vigProgr}"])
    # doc.append(NewPage())
    # with doc.create(LongTable(table_spec=r"p{0.18\textwidth}p{0.72\textwidth}",row_height=1.5)) as table:
    #         table.add_row([
    #             textcolor
    #                 (
    #                 size="12",
    #                 vspace="0",
    #                 color="parte",
    #                 bold=True,
    #                 text="2 Descripción general"
    #                 ),
    #                 f"{desGener}"
    #             ])
    #         table.add_row([
    #             textcolor
    #                 (
    #                 size="12",
    #                 vspace="0",
    #                 color="parte",
    #                 bold=True,
    #                 text="2 Objetivos"
    #                 ),
    #                 f"{objGener}"
    #             ])
    #         table.add_row([
    #             "",
    #             f"{objEspec}"
    #             ])
    doc.generate_pdf(f"./mallas/{programa}", clean=True, clean_tex=False, compiler='lualatex')


generar_malla("Electromecánica")