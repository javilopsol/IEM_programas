import os
import pandas as pd
from pylatex import Document, Package, Command, PageStyle, Head, MiniPage, StandAloneGraphic, NewPage
from pylatex.utils import italic, NoEscape

cursos = pd.read_csv("cursos.csv")
print(cursos.head())

codCurso = "MI4136"
nomCurso = cursos[cursos.Codigo == 'MI4136'].Nombre.item()

print(codCurso)
print(nomCurso)

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

    first_page = PageStyle("firstpage")

    # Header image
    with first_page.create(Head("L")) as header_left:
        with header_left.create(MiniPage(width=NoEscape(r"0.49\textwidth"),
                                         pos='l')) as logo_wrapper:
            logo_file = 'figuras/Logo.png'
            logo_wrapper.append(StandAloneGraphic(image_options="width=62.5mm",
                                filename=logo_file))

    doc.preamble.append(first_page)
    doc.change_document_style("firstpage")
    

    doc.append('Hola')
    doc.append(NewPage())
    doc.append('Hola')
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