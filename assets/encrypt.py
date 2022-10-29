from PyPDF2 import PdfFileWriter, PdfFileReader
import io


def encrypt_pdf(filename, encrypt_pass):
    pdf_writer = PdfFileWriter()
    file = PdfFileReader(filename)
    num = file.numPages

    # Read every page of the file
    for idx in range(num):
        page = file.getPage(idx)
        pdf_writer.addPage(page)

    pdf_writer.encrypt(encrypt_pass)
    io_stream = io.BytesIO()
    pdf_writer.write(io_stream)
    io_stream.seek(0)

    return io_stream
