import os
# from nltk import

def filesToCorpus(path):
    text = ''
    for file in os.listdir(path):
        if file.endswith(".txt"):
            temp = ''
            print("Adding file {} to corpus".format(file))
            fileobj = open(path + file, "r+")
            temp += fileobj.read()
            text += temp
            fileobj.close()
    if not (os.path.exists(path + "corpus/")):
        os.makedirs(path + "corpus/")
    fileobj = open(path + "corpus/corpus.txt", "w")
    print(len(text))
    fileobj.write(text)
    fileobj.close()

path = "C:/Users/shitt/Desktop/Summer Internship/Natural Language Processing (Prof. Chung)/Natural-language-processing/pdf-to-text/TextFiles/2014 (Fifteenth) Detonation Symposium/"
filesToCorpus(path)
