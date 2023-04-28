#BewareoftheFriendlyStranger
import os
import PyPDF2

# Define los nombres de los archivos INDEX_1 y INDEX_2
index1_filename = 'INDEX_1.pdf'
index2_filename = 'INDEX_2.pdf'

# Recorre todos los archivos PDF en el directorio actual
for filename in os.listdir('.'):
    if filename.endswith('.pdf') and filename != index1_filename and filename != index2_filename:
        # Abre el archivo PDF que deseas modificar
        pdf_file = open(filename, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)

        # Abre el archivo INDEX_1.pdf y agrega su contenido al inicio del archivo PDF
        index1_file = open(index1_filename, 'rb')
        index1_reader = PyPDF2.PdfFileReader(index1_file)
        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_writer.addPage(index1_reader.getPage(0))
        for page_num in range(0, pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page_num))

        # Abre el archivo INDEX_2.pdf y agrega su contenido al final del archivo PDF
        index2_file = open(index2_filename, 'rb')
        index2_reader = PyPDF2.PdfFileReader(index2_file)
        for page_num in range(0, index2_reader.getNumPages()):
            pdf_writer.addPage(index2_reader.getPage(page_num))

        # Guarda el archivo PDF modificado con el mismo nombre que tenía antes de la combinación
        output_file = open(filename, 'wb')
        pdf_writer.write(output_file)

        # Cierra todos los archivos abiertos
        output_file.close()
        pdf_file.close()
        index1_file.close()
        index2_file.close()
