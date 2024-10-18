import PyPDF2

# Abre el archivo PDF en modo lectura binaria
with open('archivo1.pdf', 'rb') as pdf_file:
    lector_pdf = PyPDF2.PdfReader(pdf_file)

    # Recorre todas las páginas y extrae el texto
    for pagina in range(len(lector_pdf.pages)):
        pagina_actual = lector_pdf.pages[pagina]
        texto = pagina_actual.extract_text()
        print(f"Texto de la página {pagina + 1}:\n{texto}\n")