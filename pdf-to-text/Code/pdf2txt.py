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
import errno


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
        """
        In pdfminer.six pdfinterp.py line 801:
        change:-
        if 'W' in obj and 'H' in obj:
        to:-
        if b'W' in obj and b'H' in obj:  //'W' and 'H' need to be byte type objects and hence conversion :)


        In pdfminer.six psparser.py line 469:
        change:-
        self._curtoken += six.int2byte(int(self.oct, 8))
        self._parse1 = self._parse_string
        return i
        to:-
        if(int(self.oct, 8) >= 0 and int(self.oct, 8) <= 255): //This check is necessary as it is invalid in some cases...
            self._curtoken += six.int2byte(int(self.oct, 8))
            self._parse1 = self._parse_string
            return i
        """
        interpreter.process_page(page)
        pageCount += 1
        print(pageCount)

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
    # for i in separators:
    #     if (i in text):
    #         text = text.split(i, 1)[0]
    #         break;
    i = 0
    while(i < len(text)):
        if (ord(text[i]) == 10 and text[i - 1] == '-'):
            line = line[: -1]
            i += 1
        elif (ord(text[i]) == 10):
            if(len(line) > 20):
                finalText += line
            line = ''
        if ((64 < ord(text[i]) < 91) or (ord(text[i]) == 10) or (47 < ord(text[i]) < 58) or (96 < ord(text[i]) < 123) or (31 < ord(text[i]) < 34)\
        or (ord(text[i]) == 63) or (44 < ord(text[i]) < 47)):
            line += text[i]
        i += 1
    return finalText
"""                     End of function                     """


"""
Path of the directories having the pdf files and the target direcotry to store the
text files

*** Change these according to the path in your system :)
"""
pdfDir = "C:/Users/shitt/Desktop/Summer Internship/Natural Language Processing (Prof. Chung)/Natural-language-processing/pdf-to-text/PDFFiles/"
txtDir = "C:/Users/shitt/Desktop/Summer Internship/Natural Language Processing (Prof. Chung)/Natural-language-processing/pdf-to-text/TextFiles/"

"""
This is the main function that carries the conversion of multiple PDFs to text file
"""
for folder in os.listdir(pdfDir):
    for file in os.listdir(pdfDir + folder):
        if(file.endswith(".pdf")):
            print("Converting: {}........".format(file))
            separators = ("Acknowledgments", "Acknowledgment", "ACKNOWLEDGEMENT", "References", "REFERENCES")
            text = convert_pdf_to_txt(pdfDir + folder + '/' + file)

            printableText = filter(text, separators)

            writeFileName = txtDir + folder  +file.replace(".pdf", ".txt")

            if not(os.path.exists(os.path.dirname(writeFileName))):
                try:
                    os.makedirs(os.path.dirname(writeFileName))
                except OSError as exc:
                    if(exc.errno != errno.EExist):
                        raise

            textFile = open(writeFileName, "w")
            textFile.write(printableText)
            textFile.close()

print("Done converting PDFs")
