import nltk
from nltk.tokenize import word_tokenize
#splite function
word="""Blockchain ensures university grades remain secure, transparent, and tamper-proof, building long-term trust in academic records.
Any attempt to alter data is instantly detected, preserving the integrity of student achievements."""
def split_function(word):
    return word.split()
print(split_function(word))
#tokenization sentence
def sentence_tokenization(word):
    return word.split('.')
print(sentence_tokenization(word))
#tokenization word
def word_tokenizationnltk(word):
    nltk.download('punkt')
    word_tokens=word_tokenize(word)
    print(word_tokens)
word_tokenizationnltk(word)