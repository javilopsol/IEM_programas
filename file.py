import os
import pandas as pd
from pylatex import Document, Package, Command
from pylatex.base_classes import Environment
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

print(horClass)

class titlepage(Environment):
    escape = False
    content_separator = "\n"




commands = NoEscape(r'''
\newcommand{\codCurso}{EM-XXXX}
\newcommand{\nomCurso}{Introducción a la arepa voladora}
\newcommand{\tipCurso}{Teórico-Práctico}
\newcommand{\elec}{No}
\newcommand{\unAcred}{Ingeniería 50\%, Diseño 50\%}
\newcommand{\ubiPlan}{X Semestre}
\newcommand{\requisito}{EM-XXX Curso X}
\newcommand{\coRequisito}{Ninguno}
\newcommand{\requiDe}{Ninguno}
\newcommand{\asist}{Asistencia Libre}
\newcommand{\sufi}{No tiene suficiencia}
\newcommand{\credito}{4}
\newcommand{\hClass}{4}
\newcommand{\hExtra}{12}
\newcommand{\vigProgra}{X Semestre 20XX}

\newcommand{\nomEscuela}{Escuela de Ingeniería Electromecánica}
\newcommand{\nomPrograma}{Licenciatura en Ingeniería Electromecánica}

\newcommand{\nomProfe}{Pepe Aguilar}
\newcommand{\corProfe}{pagui@itcr.ac.cr}
\newcommand{\consulta}{Consulta: Miércoles 7:30 a.m. – 10:30 a.m.}
''')



def main():
    geometry_options = { 
        "letterpaper": True,
        "left": "22.5mm",
        "right": "16.1mm",
        "top": "48mm",
        "bottom": "25mm",
        "headheight": "12.5mm",
        "footskip": "12.5mm"
    }
    doc = Document(documentclass="article", \
                   fontenc=None, \
                   inputenc=None, \
                   lmodern=False, \
                   textcomp=False, \
                   page_numbers=False, \
                   indent=False, \
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
    doc.packages.append(Package(name="lastpage"))
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
    doc.add_color('parte','rgb','0.02,0.204,0.404') #5,52,103
    doc.add_color('nomCur','rgb','0.02,0.455,0.773') #5,116,197
    doc.add_color('fila','rgb','0.929,0.929,0.929') #237,237,237
    doc.add_color('linea','rgb','0.749,0.749,0.749') #191,191,191


    # first_page = PageStyle("firstpage")

    # # Header image
    # with first_page.create(Head("L")) as header_left:
    #     with header_left.create(MiniPage(width=NoEscape(r"0.49\textwidth"),
    #                                      pos='l')) as logo_wrapper:
    #         logo_file = 'figuras/Logo.png'
    #         logo_wrapper.append(StandAloneGraphic(image_options="width=62.5mm",
    #                             filename=logo_file))
    
    

    #doc.preamble.append(commands)

    doc.preamble.append(Command('pagestyle','fancy'))

    headerandfooter = NoEscape(
    r'''\lhead{\begin{tikzpicture}[overlay, remember picture]
    \node[inner sep=0mm,outer sep=0mm,anchor=north west,
    xshift=18mm,
    yshift=-18mm]
    at (current page.north west)
    {\includegraphics[width=62.5mm]{figuras/Logo.png}};
    \end{tikzpicture}}
    \fancyfoot{}
    \lfoot{\textcolor{nomCur}{\nomEscuela - \nomPrograma}}
    \fancyfoot[R]{\textcolor{nomCur}{Página \thepage \hspace{1pt} de \pageref{LastPage}}}
    
    \renewcommand{\headrulewidth}{0pt}'''
    )

    doc.preamble.append(headerandfooter)
 
    # TikZNode(handle="logoportada",
    #          options={"inner sep": "0mm",
    #                   "outer sep": "0mm",
    #                   "anchor": "north west",
    #                   "xshift": "4mm",
    #                   "yshift": " -20mm"
    #          },
    #          text=NoEscape(r"\includegraphics[width=20cm]{figuras/Logo_portada.jpg}")
    #         )
    
    # TikZNodeAnchor(node_handle="logoportada",
    #                anchor_name="current page.north west")
    
    title = NoEscape(
    r'''\begin{tikzpicture}[overlay, remember picture]
    \node[inner sep=0mm,outer sep=0mm,anchor=north west,
    xshift=4mm, 
    yshift=-20mm]
    at (current page.north west)
    {\includegraphics[width=20cm]{figuras/Logo_portada.png}};
    \end{tikzpicture}

    \vspace*{170mm}

    \fontsize{14}{0}\selectfont Programa del curso \codCurso

    \fontsize{18}{25}\selectfont \textbf{\textcolor{nomCur}{\nomCurso}}

    \hspace*{10mm}\fontsize{12}{40}\selectfont \color{black!40!gray}\nomEscuela

    \hspace*{10mm}\fontsize{12}{14}\selectfont \color{black!40!gray}\nomPrograma
    '''
    )

    with doc.create(titlepage()):
        doc.append(title)
    doc.append(NoEscape(
               r'''\fontsize{14}{0}\selectfont\textbf{\textcolor{parte}{I parte: Aspectos relativos al plan de estudios}}'''
    ))
    doc.generate_pdf("example", clean=False, clean_tex=False, compiler='lualatex')


main()

# def fill_document(doc):
#     """Add a section, a subsection and some text to the document.

#     :param doc: the document
#     :type doc: :class:`pylatex.document.Document` instance
#     """
#     with doc.append('preamble.tex'):     
#         doc.create(Section('A section'))
#         doc.append('Some regular text and some ')
#         doc.append(italic('italic text. '))

#         with doc.create(Subsection('A subsection')):
#             doc.append('Also some crazy characters: $&#{}')


# if __name__ == '__main__':
#     # Basic document
#     doc = Document('basic')
#     fill_document(doc)

#     doc.generate_pdf(clean_tex=True)
#     doc.generate_tex()

#     # Document with `\maketitle` command activated
#     doc = Document()

#     doc.preamble.append(Command('title', 'Awesome Title'))
#     doc.preamble.append(Command('author', 'Anonymous author'))
#     doc.preamble.append(Command('date', NoEscape(r'\today')))
#     doc.append(NoEscape(r'\maketitle'))

#     fill_document(doc)

#     doc.generate_pdf('basic_maketitle', clean_tex=True)

#     # Add stuff to the document
#     with doc.create(Section('A second section')):
#         doc.append('Some text.')

#     doc.generate_pdf('basic_maketitle2', clean_tex=True)
#     tex = doc.dumps()  # The document as string in LaTeX syntax