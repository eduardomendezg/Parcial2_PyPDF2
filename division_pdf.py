from PyPDF2 import PdfReader, PdfWriter

# Abrir el archivo PDF que deseas dividir
with open('Plan_de_seguridad.pdf', 'rb') as pdf_file:
    # Leer el archivo PDF y obtener sus páginas
    pdf_reader = PdfReader(pdf_file)
    pages = pdf_reader.pages

    # Escribir cada página en un archivo PDF separado
    for i, page in enumerate(pages):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(page)
        output_filename = f'page_{i + 1}.pdf'
        with open(output_filename, 'wb') as output_file:
            pdf_writer.write(output_file)





"""
from pypdf import PdfReader, PdfWriter

# Abrir el archivo PDF que deseas dividir
with open('input.pdf', 'rb') as pdf_file:
    # Leer el archivo PDF y obtener sus páginas
    pdf_reader = PdfReader(pdf_file)
    total_pages = len(pdf_reader.pages)

    # Calcular el punto medio
    midpoint = total_pages // 2

    # Crear el primer archivo PDF para la primera mitad
    pdf_writer_first_half = PdfWriter()
    for i in range(midpoint):
        pdf_writer_first_half.add_page(pdf_reader.pages[i])

    # Guardar la primera mitad
    with open('first_half.pdf', 'wb') as output_file:
        pdf_writer_first_half.write(output_file)

    # Crear el segundo archivo PDF para la segunda mitad
    pdf_writer_second_half = PdfWriter()
    for i in range(midpoint, total_pages):
        pdf_writer_second_half.add_page(pdf_reader.pages[i])

    # Guardar la segunda mitad
    with open('second_half.pdf', 'wb') as output_file:
        pdf_writer_second_half.write(output_file)

"""