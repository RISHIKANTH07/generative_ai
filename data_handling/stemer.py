import nltk.stem
from nltk.stem.porter import PorterStemmer
sample_text="running runner runs easily fairfairly fairness"
#stemming using porter stemmer
def stemming_porter(text):
    return " ".join([PorterStemmer().stem(word) for word in text.split()])
print(stemming_porter(sample_text))