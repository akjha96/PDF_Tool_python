import sys
import PyPDF2

input_pdf = sys.argv[1]
watermarked_pdf = sys.argv[2]

watermarked_reader = PyPDF2.PdfFileReader(watermarked_pdf)
watermarked_page = watermarked_reader.getPage(0)

writer = PyPDF2.PdfFileWriter()

reader = PyPDF2.PdfFileReader(input_pdf)
for i in range(reader.getNumPages()):
    page = reader.getPage(i)
    page.mergePage(watermarked_page)
    writer.addPage(page)

with open('./pdfs/watermarkedpdf1.pdf', 'wb') as writefile:
    writer.write(writefile)
