# pdfquery, returns an XML file
# https://towardsdatascience.com/scrape-data-from-pdf-files-using-python-and-pdfquery-d033721c3b28

# import pdfquery
import pandas as pd
# import tika
# from tika import parser

import fitz
print(fitz.__doc__)
# https://pypi.org/project/PyMuPDF/
# https://pymupdf.readthedocs.io/en/latest/tutorial.html
def read_PDF(file_name):
    doc=fitz.open(file_name)
    for page in doc:
        text=page.get_text("text")
        # print(text)
    return text
# https://github.com/chrismattmann/tika-python
def extract_to_text(file_name):
    parsed=parser.from_file(f'{file_name}');
    print(parsed["metadata"])
    print(parsed["content"])

#PyPDF2
# https://www.geeksforgeeks.org/extract-text-from-pdf-file-using-python/
def extract(file_name):
    pdf = pdfquery.PDFQuery(file_name)
    pdf.load()
    pdf.tree.write(f'{file_name}.xml', pretty_print = True)

# extract("timetable.pdf")
# extract_to_text("LIN_XINLEI_Short_Resume (english version).pdf")
# read_PDF("LIN_XINLEI_Short_Resume (english version).pdf")