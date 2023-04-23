from PyPDF2 import PdfFileWriter, PdfFileReader

input_pdf = PdfFileReader(open("input.pdf", "rb"))
output_pdf = PdfFileWriter()

for i in range(0, input_pdf.getNumPages(), 2):
    left_page = input_pdf.getPage(i)
    right_page = input_pdf.getPage(i+1)

    new_page = PdfFileWriter()
    new_page.addPage(right_page)
    new_page.addPage(left_page)

    new_page.mediaBox.upperRight = (350, 250)
    output_pdf.addPage(new_page.getPage(0))

with open("output.pdf", "wb") as out_f:
    output_pdf.write(out_f)
