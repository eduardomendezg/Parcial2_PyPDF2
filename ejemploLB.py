import PyPDF2


def leer_pdf(ruta_pdf):
    with open(ruta_pdf, 'rb') as archivo_pdf:
        lector_pdf = PyPDF2.PdfReader(archivo_pdf)
        numero_paginas = len(lector_pdf.pages)
        texto = ""
        for pagina in range(numero_paginas):
            texto += lector_pdf.pages[pagina].extract_text()
        return texto


def copiar_pdf(archivo_origen, archivo_destino):
    with open(archivo_origen, 'rb') as origen, open(archivo_destino, 'wb') as destino:
        lector_pdf = PyPDF2.PdfReader(origen)
        escritor_pdf = PyPDF2.PdfWriter()
        
        for pagina in lector_pdf.pages:
            escritor_pdf.add_page(pagina)
        
        escritor_pdf.write(destino)


def fusionar_pdfs(lista_pdfs, salida):
    escritor_pdf = PyPDF2.PdfWriter()
    
    for ruta_pdf in lista_pdfs:
        with open(ruta_pdf, 'rb') as archivo_pdf:
            lector_pdf = PyPDF2.PdfReader(archivo_pdf)
            for pagina in lector_pdf.pages:
                escritor_pdf.add_page(pagina)
    
    with open(salida, 'wb') as archivo_salida:
        escritor_pdf.write(archivo_salida)

ruta_pdf = 'ejemplo1.pdf'
contenido = leer_pdf(ruta_pdf)
print("Contenido del PDF:")
print(contenido)


archivo_origen = 'ejemplo1.pdf'
archivo_destino = 'copia_ejemplo1.pdf'
copiar_pdf(archivo_origen, archivo_destino)
print(f"Archivo {archivo_destino} creado correctamente.")


lista_pdfs = ['ejemplo1.pdf', 'ejemplo2.pdf']
archivo_fusionado = 'fusionado.pdf'
fusionar_pdfs(lista_pdfs, archivo_fusionado)
print(f"Archivos fusionados en {archivo_fusionado}.")
