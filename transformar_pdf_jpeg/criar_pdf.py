from PyPDF2 import PdfWriter, PdfReader

# Carregar um PDF vazio ou existente, se disponível
pdf_writer = PdfWriter()

# Carregar uma página de outro PDF (se aplicável)
# Por exemplo:
pdf_reader = PdfReader("modelo.pdf")  # Supondo que você tenha um PDF modelo com uma página
page = pdf_reader.pages[0]  # Pegando a primeira página do modelo
pdf_writer.add_page(page)

# Salvar o PDF com a nova página adicionada
with open("meu_arquivo.pdf", "wb") as output_pdf:
    pdf_writer.write(output_pdf)
