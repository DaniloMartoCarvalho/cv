#!/usr/bin/env python3

"""
Esse script gera o meu C.V. baseado no modelo './templates/template.docx' usando os
dados fornecidos pelo módulo './datas.py'
"""

from docxtpl import DocxTemplate
from datas import datas


if __name__ == "__main__":
    context = datas

    doc = DocxTemplate(r"./templates/template.docx")

    doc.render(context)

    doc.save(r"./cv.docx")
