import glob, os, shutil
from PyPDF2 import PdfFileReader # pip install pypdf2

# Copies of all PDF files inside the 'path_in' directory which contain ALL strings in 'keywords'
# These copies are sent to the 'path_out' directory
# This is not a perfect search, as the PyPDF2 PdfFileReader object does not find all text
def PDF_Search_All(path_in, path_out, keywords):
    if not os.path.isdir(path_in):
        print("Input Directory Invalid: ", path_in)
        return
    elif len(keywords) == 0:
        print("Keywords List Size Invalid: 0")
        return
    elif not os.path.isdir(path_out):
        os.mkdir(os.path.join(path_out))

    for pdf in glob.glob(path_in + "/**/*.pdf", recursive=True):
        with open(pdf, 'rb') as file:
            if file:
                ipdf = PdfFileReader(file)
                found = [0] * len(keywords)
                for chunk in [p.extractText() for p in ipdf.pages]:
                    chunk_found = [not chunk.find(key) == -1 for key in keywords]
                    found = [a or b for a, b in zip(found, chunk_found)]
                if not 0 in found:
                    shutil.copy(pdf, path_out)

# Copies of all PDF files inside the 'path_in' directory which contain ANY strings in 'keywords'
# These copies are sent to the 'path_out' directory
# This is not a perfect search, as the PyPDF2 PdfFileReader object does not find all text
def PDF_Search_Any(path_in, path_out, keywords):
    if not os.path.isdir(path_in):
        print("Input Directory Invalid: ", path_in)
        return
    elif len(keywords) == 0:
        print("Keywords List Size Invalid: 0")
        return
    elif not os.path.isdir(path_out):
        os.mkdir(os.path.join(path_out))

    for pdf in glob.glob(path_in + "/**/*.pdf", recursive=True):
        with open(pdf, 'rb') as file:
            if file:
                ipdf = PdfFileReader(file)
                for chunk in [p.extractText() for p in ipdf.pages]:
                    found = [not chunk.find(key) == -1 for key in keywords]
                    if any(not chunk.find(key) == -1 for key in keywords):
                        shutil.copy(pdf, path_out)
                        break
