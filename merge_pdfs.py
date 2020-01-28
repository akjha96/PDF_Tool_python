import PyPDF2
import sys

inputs = sys.argv[1:]
print(inputs)


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        # clean_name = os.path.basename(pdf)
        # print(clean_name)
        print(pdf)
        merger.append(pdf)
    merger.write("./pdfs/Super1.pdf")


pdf_combiner(inputs)
