import os
import fitz  # PyMuPDF

def pdf_to_images(pdf_path, output_folder):
    pdf_document = fitz.open(f'media/{pdf_path}')

    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        pix = page.get_pixmap(dpi=144)
        output_file = f"{output_folder}/page_{page_num + 1}.png"
        pix.save(output_file)

    pdf_document.close()