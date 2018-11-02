# from nltk import word_tokenizer
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
from gensim.parsing.preprocessing import STOPWORDS as stop_words
from collections import Counter
from nltk.stem import WordNetLemmatizer
import string

import re


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def remove_punc(str):
    punctuations = set(string.punctuation) - {".", "-"}
    str = list(str)
    str = [alphabet for alphabet in str if alphabet not in punctuations]
    return ''.join(str)


def load_text_data(data_path):
    file_object = open(data_path, "r+")
    text = file_object.read()
    file_object.close()
    return text

def lemmatize_word(word):
    wordnet_lemmatizer = WordNetLemmatizer()
    new_word = wordnet_lemmatizer.lemmatize(word, pos="v")
    if (new_word == word):
        new_word = wordnet_lemmatizer.lemmatize(word, pos="n")
    return(new_word)


def attach_hyphens(text):
    text = text.split()
    temp = []
    length = len(text)
    for i in range(length):
        if(text[i][-1] == "-" and i+1 < length):

            temp.append(text[i][:-1] + text[i + 1])
        else:
            temp.append(text[i])
    return ' '.join(temp);

def remove_irrelevant_details(text):
    """
    Removes all punctuations excepts hyphen(-) and fullstop(.)
    """
    separators = ["References", "REFERENCES"]
    for separator in separators:
        if (separator in text):
            text = text.split(separator)[0]
            break;
    text = remove_punc(text)
    text =  ' '.join([lemmatize_word(word) for word in text.split() if word.lower() \
        not in stop_words and not is_number(word) and len(word) > 1])
    text = attach_hyphens(text)
    return text


def write_processed_text(path, text):
    file_object = open(path, "w")
    print(text)
    file_object.write(text)
    file_object.close()
    return;


txt_path = "Kamlet_Jacobs_DFT_Literature.txt"
text= load_text_data(txt_path)
text = remove_irrelevant_details(text)
write_processed_text(txt_path, text)
