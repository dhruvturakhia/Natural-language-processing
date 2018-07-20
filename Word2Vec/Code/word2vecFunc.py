from nltk.corpus import stopwords
import nltk.tokenize as tokenize
from gensim.models import Word2Vec, KeyedVectors



def getWordLessThan(corpus, reqFreq = 1, viewFlag = False):
    wordFreq = {}
    for word in corpus.split():
        if word not in wordFreq:
            wordFreq[word] = 1
        else:
            wordFreq[word] += 1
    print("Generating list of words with frequencies less than {}".format(reqFreq))
    listOfWords = []
    for key in list(wordFreq.keys()):
        if (wordFreq[key] < reqFreq):
            listOfWords.append(key)
        if(viewFlag):
            print(key)
    return wordFreq, listOfWords;





def cleanAndToken(path, minFreq = 2):
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
        filteredSentence = [w for w in tokenizedWords if not w in stopWords]
        filteredSentences.append(filteredSentence)
    return filteredSentences;

def readTextFile(path):
    print("Fetching corpus........")
    file = open(path, "r")
    text = file.read()
    file.close()
    return text;


def generateModel(readPath, modelPath, window = 6, min_count = 4):
    filteredSentences = cleanAndToken(readPath, minFreq = 23)
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




readPath = "C:/Users/shitt/Desktop/Summer Internship/Natural Language Processing (Prof. Chung)/Natural-language-processing/Word2Vec/Corpus/corpus.txt"
modelPath = "2014DetSymp.bin"
# generateModel(readPath = readPath, modelPath = modelPath)
wordFreq, dummy = getWordLessThan(readTextFile(readPath))
print(wordFreq['diagram'])
# print(useModelVec(modelPath, positiveWords = ["RDX"], mostSimilarFlag = True))
