
"""
The modules required to import
"""
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os
import errno
import string



"""
Function to convert a pdf to text using pdfminer.six
Input: path of the file: string
Output: pdf converted totext: string
"""
def convert_pdf_to_txt(path):
    pageCount = 0
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
        pageCount += 1
    text = retstr.getvalue()
    fp.close()
    device.close()
    retstr.close()
    return text
"""                     End of function                     """


def writeToFile (path, text):
    if not(os.path.exists(os.path.dirname(path))):
        try:
            os.makedirs(os.path.dirname([path]))
        except OSError as exc:
            print("here")
            if(exc.errno != errno.EExist):
                raise

    text = (text.encode('ascii', errors = 'ignore')).decode()
    textFile = open(path, "w")
    textFile.write(text)
    textFile.close()


"""
Converts all pdfs in a directory and all its branch/sub directories to text
input:
str: path to the directory with the pdf Files
str: path to store the text files if __name__ == '__main__':
"""

def convert_multiple_pdfs(pdfDir, txtDir):
    printable = set(string.printable)
    for file in os.listdir(pdfDir):
        if(os.path.isdir(pdfDir + "/" + file)):
            convert_multiple_pdfs(pdfDir + "/" + file, txtDir + "/" + file)
        if(file.endswith(".pdf")):
            print("Converting: {}........".format(file))
            text = convert_pdf_to_txt(pdfDir + '/' + file)
            writeFileName = txtDir + "/text/" + file.replace(".pdf", ".txt")
            writeToFile(writeFileName, text)

"""                     End of function                     """



pdfDir = "C:/Users/shitt/Desktop/Natural Language Processing (Prof. Chung)/Natural-language-processing/Original approach/pdf-to-text/PDFFiles/Text Books"
txtDir = "C:/Users/shitt/Desktop/Natural Language Processing (Prof. Chung)/Natural-language-processing/Hierarchical approach/Topic Modeling/Text Files/Text Books"

convert_multiple_pdfs(pdfDir, txtDir)
