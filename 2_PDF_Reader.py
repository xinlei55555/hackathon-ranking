# pdfquery, returns an XML file
# https://towardsdatascience.com/scrape-data-from-pdf-files-using-python-and-pdfquery-d033721c3b28

#PyPDF2
# https://www.geeksforgeeks.org/extract-text-from-pdf-file-using-python/
import pdfquery
import pandas as pd

def extract(file_name):
    pdf = pdfquery.PDFQuery(file_name)
    pdf.load()
    pdf.tree.write(f'{file_name}.txt', pretty_print = True)
