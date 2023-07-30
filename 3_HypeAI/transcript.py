import PyPDF2

with open("timetable.pdf", "rb") as pdf_file:
    print(pdf_file)
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    page = read_pdf.pages[0]
    page_content = page.extractText()
print(page_content)