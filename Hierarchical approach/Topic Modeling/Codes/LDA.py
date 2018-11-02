import gensim
from nltk.tokenize import sent_tokenize, word_tokenize
from gensim import corpora
import numpy as np



#Get The data
def load_Data(data_path):
    data_file = open(data_path, "r+")
    return data_file.read()


def pre_process(data):
    preprocessed_data = []
    sent_docs = sent_tokenize(data)
    for sentence in sent_docs:
        sent = [token for token in word_tokenize(sentence) if token != "."]
        preprocessed_data.append(sent)
    return preprocessed_data

# path = "Kamlet_Jacobs_DFT_Literature.txt"
# save_file = "Kamlet_Jacobs"
# docs = load_Data(path)
# processed_docs = pre_process(docs)
# dictionary = corpora.Dictionary(processed_docs)
# doc_term_matrix = [dictionary.doc2bow(doc) for doc in processed_docs]
Lda = gensim.models.ldamodel.LdaModel
# # Running and Training LDA model on the document term matrix.
# ldamodel = Lda(doc_term_matrix, num_topics=5, id2word = dictionary, passes=50)
# ldamodel.save(save_file)


save_file= "Kamlet_Jacobs"
ldamodel = Lda.load(save_file)
print("\n\n", save_file)
for topic in ldamodel.print_topics(num_topics=5):
    print(topic)
save_file = "ICT 2014"
ldamodel = Lda.load(save_file)
print("\n\n", save_file)
for topic in ldamodel.print_topics(num_topics=5):
    print(topic)
save_file = "IDS_2014"
ldamodel = Lda.load(save_file)
print("\n\n", save_file)
for topic in ldamodel.print_topics(num_topics=5):
    print(topic)
