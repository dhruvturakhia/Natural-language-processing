"""
@author: Dhruv Turakhia
Program to convert multiple research paper pdfs in a directory
to text files
"""

#Ignore the below comment if you just want to run the code :P

"""
    ***         ***
   *****       *****
    ***         ***

    ***         ***
      ***********

The world was ruled by PDF, but he was stubborn and inflexible and did not help
the people from NLP :( They wanted to work to make a the world a simple place to
understand. So now we begin a journey to change these stubborn people to be flexible
and help us understand the teachings of the great :D
"""

"""
There will be a feedback document in the repository as well, if you are uncomfortable
with the style of my comments or anything else please let me know :D
"""


""" Import required modules for execution """

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os


""" Function to convert a pdf to text using pdfminer.six
    Input: path of the file: string
    Output: pdf converted totext: string
"""
def convert_pdf_to_txt(path):
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

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text
"""                     End of function                     """


""" This is a custom filter function which takes in a string text file and a list
    of separators(generally includes words like references/acknowledgements) and
    outputs a filtered text without references and rid of 90% irrelevant data

    Input: text: string, separators: list of strings
    Output: filtered text: string """

def filter(text = '', separators = []):
    finalText, line = '', ''
    for i in separators:
        if (i in text):
            text = text.split(i, 1)[0]
            break;
    i = 0
    while(i < len(text)):
        if (ord(text[i]) == 10 and text[i - 1] == '-'):
            line = line[: -1]
            i += 1
        elif (ord(text[i]) == 10):
            if(len(line) > 20):
                finalText += line
            line = ''
        if ((31 < ord(text[i]) < 127) or (ord(text[i]) == 10)):
            line += text[i]
        i += 1
    return finalText
"""                     End of function                     """


"""
Path of the directories having the pdf files and the target direcotry to store the
text files

*** Change these according to the path in your system :)
"""
pdfDir = "C:/Users/Dhruv/Desktop/Summer Internship/Natural Language Processing (Prof. Chung)/Natural-language-processing/pdf-to-text/PDFFiles/2014 (Fifteenth) Detonation Symposium/"
txtDir = "C:/Users/Dhruv/Desktop/Summer Internship/Natural Language Processing (Prof. Chung)/Natural-language-processing/pdf-to-text/TextFiles/2014 (Fifteenth) Detonation Symposium/"

"""
This is the main function that carries the conversion of multiple PDFs to text file
"""
for file in os.listdir(pdfDir):
    if(file.endswith(".pdf")):
        print("Converting: {}........".format(file))
        separators = ("Acknowledgments", "Acknowledgment", "ACKNOWLEDGEMENT", "References", "REFERENCES")
        text = convert_pdf_to_txt(pdfDir + file)

        printableText = filter(text, separators)

        writeFileName = txtDir + file.replace(".pdf", ".txt")
        textFile = open(writeFileName, "w")
        textFile.write(printableText)
        textFile.close()

print("Done converting PDFs")
