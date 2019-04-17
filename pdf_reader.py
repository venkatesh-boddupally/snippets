import PyPDF2


def get_pdf_content_lines(pdf_file_path):
    with open(pdf_file_path, 'rb') as pdf_file:
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        for page in read_pdf.pages:
            for out_line in page.extractText().splitlines():
                yield out_line


for line in get_pdf_content_lines('pdf/file/path'):
    print(line)
