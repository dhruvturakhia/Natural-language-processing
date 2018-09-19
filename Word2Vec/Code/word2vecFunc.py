from nltk.corpus import stopwords
import nltk.tokenize as tokenize
from gensim.models import Word2Vec, KeyedVectors
import nltk



def getWordLessThan(corpus, reqFreq = 1, viewFlag = False):
    wordFreq = {}
    for word in corpus.split():
        if word not in wordFreq:
            wordFreq[word] = 1
        else:
            wordFreq[word] += 1
    print("Generating list of words with frequencies more than {}".format(reqFreq))
    listOfWords = []
    for key in list(wordFreq.keys()):
        if (wordFreq[key] < reqFreq):
            listOfWords.append(key)
        if(viewFlag):
            print(key)
    return wordFreq, listOfWords;




def cleanAndToken(path, minFreq = 1, forTagging = False):
    corpus = readTextFile(path)
    filteredSentences = []
    dummy, listOfWords = getWordLessThan(corpus, reqFreq = minFreq)
    print("Modifying stopwords.......")
    stopWords = stopwords.words('english')
    stopWords += listOfWords
    stopWords = set(stopWords)
    sentences = tokenize.sent_tokenize(corpus)
    corpus.encode('utf-8').strip()

    print("Tokenizing corpus and removing stop words........")
    for sentence in sentences:
        tokenizedWords = tokenize.word_tokenize(sentence)
        if (not forTagging):
            filteredSentence = [w for w in tokenizedWords if not w.lower() in stopWords and (len(w) > 1) and not w.isdigit()]
        else:
            filteredSentence = tokenizedWords
        filteredSentences.append(filteredSentence)
    return filteredSentences;




def readTextFile(path):
    print("Fetching corpus........")
    file = open(path, "r")
    text = file.read()
    file.close()
    return text;




def generateModel(readPath, modelPath, window = 6, min_count = 4):
    filteredSentences = cleanAndToken(readPath)
    print("Generating the word2vec model with a window of {win} and minimum count of {min_cnt}........".format(win = window, min_cnt = min_count))
    model = Word2Vec(filteredSentences, window, min_count)
    print("Saving model in \n{}........".format(modelPath))
    model.save(modelPath)
    return True;




def useModelVec(modelPath, positiveWords = [], negativeWords = [], similarWords = [],\
                mostSimilarFlag = False, similarityFlag = False):
    model = KeyedVectors.load(modelPath)
    if(mostSimilarFlag):
        return(model.most_similar(positive = positiveWords, negative = negativeWords))
    elif(similarityFlag):
        return(model.similarity(similarWords[0], similarWords[1]))
    else:
        print("No functionality was requested........")
        return 0;




def useModelVocab(modelPath, vocabCountFlag = False):
    model = KeyedVectors.load(modelPath)
    if(vocabCountFlag):
        return(len(model.wv.vocab));
    else:
        print("No requests made........")


def posSmallText(readPath, sentenceNum = 0, showSingleSent = False):
    taggedList = []
    sentences = cleanAndToken(readPath, forTagging = True)
    for sentence in sentences:
        taggedList.append(nltk.pos_tag(sentence))

    if(showSingleSent):
        if(sentenceNum >= len(sentences)):
            print("Sorry, the sentence number is greater than total sentences")
            print("Printing the last sentence")
            print(taggedList[len(sentences) - 1])
        elif(sentenceNum < 0):
            print("Sorry, the sentence number is less than 0")
            print("Printing the first tagged sentence")
            print(taggedList[len(sentences) - 1])
        else:
            print("Printing the {} tagged sentence".format(sentenceNum))
            print(taggedList[sentenceNum])

    else:
        print("Printing the complete list")
        print(taggedList)




"""
Using:
Perceptron Tagger (nltk) :)

TODO:
ChemDataExtractor: Get nameList

WordNet: for lexical filtering + Word2vec: filtering using sum/minus

Subject-verb-object (Typed dependancies)

Stanford Parser JAVA


Look into:
Probabilistic Embeddings

Hierarichal Probabilistic approach
"""




readPath = "C:/Users/shitt/Desktop/Natural Language Processing (Prof. Chung)/Natural-language-processing/Corpus/corpus.txt"
taggingReadPath = "C:/Users/shitt/Desktop/Natural Language Processing (Prof. Chung)/Natural-language-processing/pdf-to-text/TextFiles/ICT 2008/V001.txt"
modelPath = "fullCorpusVec.bin"
# generateModel(readPath = readPath, modelPath = modelPath)
# wordFreq, dummy = getWordLessThan(readTextFile(readPath))
# print(useModelVec(modelPath, similarWords = [], similarityFlag = True))
# print(model.wv.vocab)
posSmallText(taggingReadPath, sentenceNum = 5, showSingleSent = True)
