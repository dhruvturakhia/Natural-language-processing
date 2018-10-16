import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
from nltk.tokenize import sent_tokenize, word_tokenize
from gensim import corpora
import numpy as np



#Get The data
def load_Data(data_path):
    data_file = open(data_path, "r+")
    return data_file.read()

def lemmatize_stemming(data):
    return SnowballStemmer.stem(WordNetLemmatizer().lemmatize(data, pos='v'))

def pre_process(data):
    preprocessed_data = []
    sent_docs = sent_tokenize(data)
    for sentence in sent_docs:
        sent = [token for token in word_tokenize(sentence) if token.lower() not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3]
        preprocessed_data.append(sent)
    return preprocessed_data

path = "C:/Users/shitt/Desktop/Natural Language Processing (Prof. Chung)/\
Natural-language-processing/Hierarchical approach/Topic Modeling/Corpuses/\
2014 (Fifteenth) Detonation Symposium.txt"
docs = load_data(path)
processed_docs = pre_process(docs)
dictionary = corpora.Dictionary(processed_docs)
doc_term_matrix = [dictionary.doc2bow(doc) for doc in processed_docs]
Lda = gensim.models.ldamodel.LdaModel
# Running and Trainign LDA model on the document term matrix.
ldamodel = Lda(doc_term_matrix, num_topics=3, id2word = dictionary, passes=50)
print(ldamodel.print_topics(num_topics=10, num_words=10))
