# from nltk import word_tokenizer
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
from gensim.parsing.preprocessing import STOPWORDS as stop_words


import regex as re


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def load_text_data(data_path):
    file_object = open(data_path, "r+")
    return file_object.read()

def remove_irrelevant_details(text):
    """
    Removes all punctuations excepts hyphen(-) and fullstop(.)
    """
    text = re.sub(r"[^\P{P}-.]+", "", text)
    text = [word for word in text.split() if word.lower() \
        not in stop_words and not is_number(word) and len(word) > 1]


txt_path = "temp.txt"
text= load_text_data(txt_path)
remove_irrelevant_details(text)
