import os
import pandas as pd
from pylatex import Document, Package, Command, PageStyle, Head, MiniPage, StandAloneGraphic, NewPage, TikZNode, TikZNodeAnchor
from pylatex.base_classes import Environment
from pylatex.utils import italic, NoEscape

cursos = pd.read_csv("cursos.csv")
print(cursos.head())

codCurso = "MI4136"
nomCurso = cursos[cursos.Codigo == 'MI4136'].Nombre.item()

print(codCurso)
print(nomCurso)

class titlepage(Environment):
    escape = False
    content_separator = "\n"

def main():
    geometry_options = {
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
    doc.packages.append(Package(name="fontspec", options=None))
    doc.preamble.append(Command('setmainfont','Arial'))
    doc.packages.append(Package(name="babel", options=['spanish',"activeacute"]))
    doc.packages.append(Package(name="graphicx"))
    doc.packages.append(Package(name="tikz"))
    doc.preamble.append(Command('usetikzlibrary','calc'))
    doc.packages.append(Package(name="anyfontsize"))
    doc.packages.append(Package(name="xcolor"))
    doc.packages.append(Package(name="colortbl"))
    doc.add_color('parte','rgb','0.02,0.204,0.404') #5,52,103
    doc.add_color('nomCur','rgb','0.02,0.455,0.773') #5,116,197
    doc.add_color('fila','rgb','0.929,0.929,0.929') #237,237,237
    doc.add_color('linea','rgb','0.749,0.749,0.749') #191,191,191
    doc.packages.append(Package(name="array"))
    doc.packages.append(Package(name="float"))
    doc.packages.append(Package(name="lastpage"))
    doc.packages.append(Package(name="longtable"))
    doc.packages.append(Package(name="multirow"))
    doc.packages.append(Package(name="fancyhdr"))
    # first_page = PageStyle("firstpage")

    # # Header image
    # with first_page.create(Head("L")) as header_left:
    #     with header_left.create(MiniPage(width=NoEscape(r"0.49\textwidth"),
    #                                      pos='l')) as logo_wrapper:
    #         logo_file = 'figuras/Logo.png'
    #         logo_wrapper.append(StandAloneGraphic(image_options="width=62.5mm",
    #                             filename=logo_file))


    commands = NoEscape(
    r'''\newcommand{\codCurso}{EM-XXXX}
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
    \newcommand{\consulta}{Consulta: Miércoles 7:30 a.m. – 10:30 a.m.}'''
    )

    doc.preamble.append(commands)

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
    {\includegraphics[width=20cm]{figuras/Logo_portada.jpg}};
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
    doc.generate_pdf("example", clean_tex=False, compiler='lualatex')

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