from pdf2image import convert_from_path

pdf_path = "./pdfs/a.pdf"

pages = convert_from_path(pdf_path, 300)

for i, page in enumerate(pages):
    page.save(f"pagina){i + 1}.jpeg," "JPEG")