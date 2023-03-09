#!/usr/bin/env python3

"""
Esse script lê um C.V template dentro do diretório './templates' e substitui todos os
seus placeholder baseado nos dados fornecidos pelo módulo './datas.py'
"""

from docxtpl import DocxTemplate
from datas import datas


if __name__ == "__main__":
    context = datas

    doc = DocxTemplate(r"./templates/template.docx")

    doc.render(context)

    doc.save(r"./cv.docx")
