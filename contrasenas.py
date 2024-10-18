import PyPDF2

# Pedir la contraseña al usuario
password = input("Introduce la contraseña: ")

# Abrir el archivo PDF existente
with open("Plan_de_seguridad.pdf", "rb") as archivo:
    # Crear un lector PDF
    lector = PyPDF2.PdfReader(archivo)
    
    # Crear un escritor PDF
    escritor = PyPDF2.PdfWriter()
    
    # Añadir todas las páginas al escritor
    for pagina in range(len(lector.pages)):
        escritor.add_page(lector.pages[pagina])
    
    # Establecer la contraseña
    escritor.encrypt(password)
    
    # Guardar el nuevo archivo PDF con contraseña
    with open("archivo_protegido.pdf", "wb") as archivo_salida:
        escritor.write(archivo_salida)

print("Contraseña añadida al PDF exitosamente.")

"""
import PyPDF2

# Ruta del archivo PDF protegido
ruta_pdf_protegido = 'archivo_protegido.pdf'
# Contraseña del PDF
contrasena = 'tu_contrasena'

# Abrir el archivo PDF
with open(ruta_pdf_protegido, 'rb') as archivo:
    lector_pdf = PyPDF2.PdfReader(archivo)

    # Verificar si el PDF está cifrado
    if lector_pdf.is_encrypted:
        # Intentar descifrar el PDF
        if lector_pdf.decrypt(contrasena):
            print("PDF descifrado con éxito.")
            
            # Guardar el PDF descifrado
            with open('archivo_descifrado.pdf', 'wb') as archivo_descifrado:
                escritor_pdf = PyPDF2.PdfWriter()
                for pagina in range(len(lector_pdf.pages)):
                    escritor_pdf.add_page(lector_pdf.pages[pagina])
                escritor_pdf.write(archivo_descifrado)
        else:
            print("La contraseña es incorrecta.")
    else:
        print("El PDF no está cifrado.")

"""