"""
@author: Dhruv Turakhia
Program compile all the textfiles in a folder and generate
a corpus of them
"""

#Ignore the comment below if you just want to run the code :P
"""
So we begin the gathering of forces, the forces to find the
long lost chemical names, hidden deep in the caves of the
archives of energetic caves.
"""


""" Importing required modules for execution"""
import os


"""
Function to combine all textfiles in all the folders in a givendirectory
into a corpus and store it in the mentioned path
Input: readPath: str, writePath: str
Output: N/A


*Note:- Read Path Format: Dir--->Sub-Dir(Containing the text files)--->TextFiles
"""
def filesToCorpus(readPath, writePath):
    text = ''
    for folder in os.listdir(readPath):
        for file in os.listdir(readPath + folder):
            if file.endswith(".txt"):
                temp = ''
                print("Adding file {} to corpus".format(file))
                fileobj = open(path + file, "r+")
                temp += fileobj.read()
                text += temp
                fileobj.close()
    if not (os.path.exists(writePath + "corpus/")):
        os.makedirs(writePath + "corpus/")
    fileobj = open(path + "corpus/corpus.txt", "w")
    print(len(text))
    fileobj.write(text)
    fileobj.close()
    return;

"""                End of Function              """

"""
Main Code: Mention the read path and write path here and then generate the corpus 
"""
readPath = "C:/Users/shitt/Desktop/Summer Internship/Natural Language Processing (Prof. Chung)/Natural-language-processing/pdf-to-text/TextFiles/NTREM Proceedings/"
writePath = "C:/Users/shitt/Desktop/Summer Internship/Natural Language Processing (Prof. Chung)/Natural-language-processing/"


filesToCorpus(readPath, writePath)
