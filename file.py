import os
import pandas as pd
from pylatex import Document, Package, Command, PageStyle, Head, Foot, NewPage,\
    TextColor, MiniPage, StandAloneGraphic, simple_page_number,\
    TikZ, TikZNode, TikZOptions, TikZCoordinate, TikZNodeAnchor, TikZPath,\
    UnsafeCommand,\
    VerticalSpace, HorizontalSpace, NewLine
from pylatex.base_classes import Environment, Arguments
from pylatex.utils import italic, NoEscape

cursos = pd.read_csv("cursos.csv")
datos_gen = pd.read_csv("datos_gen.csv")

codCurso = "MI4136"
nomEscue = "Escuela de Ingeniería Electromecánica"
nomProgr = cursos[cursos.Codigo == codCurso].Programa.item()
nomCurso = cursos[cursos.Codigo == codCurso].Nombre.item()
tipCurso = datos_gen[datos_gen.Codigo == codCurso].Tipo.item()
eleCurso = datos_gen[datos_gen.Codigo == codCurso].Electivo.item()
uniAcred = datos_gen[datos_gen.Codigo == codCurso].AreasCurriculares.item()
ubiPlane = datos_gen[datos_gen.Codigo == codCurso].Ubicacion.item()
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
nomProfe = "Juan José Rojas Hernández"
corProfe = "juan.rojas@itcr.ac.cr"
conProfe = "Miercoles 7:30 a.m. - 10: 30 a.m." #Esto seria mejor construirlo tambien 


def textcolor(size,vspace,color,bold,text,hspace="0"):
    dump = NoEscape("")
    if hspace!="0":
        dump += NoEscape(HorizontalSpace(hspace,star=True).dumps())
    dump += NoEscape(Command("fontsize",arguments=Arguments(size,vspace)).dumps())
    dump += NoEscape(Command("selectfont").dumps()) + NoEscape(" ")
    if bold==True:
        dump += NoEscape(Command("textbf", NoEscape(Command("textcolor",arguments=Arguments(color,text)).dumps())).dumps())
    else:
        dump += NoEscape(Command("textcolor",arguments=Arguments(color,text)).dumps())
    return dump



# class titlepage(Environment):
#     escape = False
#     content_separator = "\n"

def main():
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
    #Variables
    doc.set_variable("nomEscue",nomEscue)
    doc.set_variable("nomProgr",nomProgr)
    doc.set_variable("codCurso",codCurso)
    doc.set_variable("nomCurso",nomCurso)
    doc.set_variable("tipCurso",tipCurso)
    doc.set_variable("eleCurso",eleCurso)
    doc.set_variable("uniAcred",uniAcred)
    doc.set_variable("ubiPlane",ubiPlane)
    doc.set_variable("susRequi",susRequi)
    doc.set_variable("corRequi",corRequi)
    doc.set_variable("essRequi",essRequi)
    doc.set_variable("tipAsist",tipAsist)
    doc.set_variable("posRecon",posRecon)
    doc.set_variable("posSufic",posSufic)
    doc.set_variable("numCredi",numCredi)
    doc.set_variable("horClass",horClass)
    doc.set_variable("horExtra",horExtra)
    doc.set_variable("vigProgr",vigProgr)
    doc.set_variable("nomProfe",nomProfe)
    doc.set_variable("corProfe",corProfe)
    doc.set_variable("conProfe",conProfe)
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
            logobox.append(StandAloneGraphic(image_options="width=62.5mm", filename='figuras/Logo.png'))
    #Left foot
    with headerfooter.create(Foot("L")) as footer_left:
        footer_left.append(TextColor("azulsuaveTEC", f"{nomEscue} - {nomProgr}"))
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
    with doc.create(TikZ(\
            options=TikZOptions(    "overlay",
                                    "remember picture"
                  
                                )
        )) as logo:
        logo.append(TikZNode(\
            options=TikZOptions(    "inner sep = 0mm",
                                    "outer sep = 0mm",
                                    "anchor = north west",
                                    "xshift = -18mm",
                                    "yshift = 32mm"
                                ),
            text=StandAloneGraphic(image_options="width=20cm", filename='figuras/Logo_portada.png').dumps(),\
            at=TikZCoordinate(0,0)
        ))
    doc.append(VerticalSpace("170mm", star=True))
    doc.append(NewLine())
    doc.append(textcolor
                (   
                size="14",
                vspace="0",
                color="black",
                bold=False,
                text=f"Programa del curso {codCurso}" 
                ))
    doc.append(NewLine())
    doc.append(textcolor
                (  
                size="18",
                vspace="25",
                color="azulsuaveTEC",
                bold=True,
                text=f"{nomCurso}" 
                ))
    doc.append(NewLine())
    doc.append(textcolor
                (
                hspace="10mm",   
                size="12",
                vspace="40",
                color="gris",
                bold=False,
                text=f"{nomEscue}" 
                ))
    doc.append(NewLine())
    doc.append(textcolor
                (   
                hspace="10mm",
                size="12",
                vspace="14",
                color="gris",
                bold=False,
                text=f"{nomProgr}" 
                ))
    doc.append(NewLine())
    doc.append(NewPage())
    doc.change_page_style("headfoot")
    doc.append(textcolor
                (   
                size="14",
                vspace="0",
                color="parte",
                bold=True,
                text="I parte: Aspectos relativos al plan de estudios"
                ))
    doc.generate_pdf("example", clean=False, clean_tex=False, compiler='lualatex')

# print(TikZNodeAnchor("current page","north west").dumps())

# print(TikZPath([current page.north west]).dumps())
main()