import PyPDF2

def count_pages_in_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        return len(pdf_reader.pages)


pdf_path =  r"C:\Users\eduar\Documents\Proyectos python\python-kevin-mendez\ejemplo1.pdf"

num_paginas = count_pages_in_pdf(pdf_path)
print(f"El PDF tiene {num_paginas} páginas.")