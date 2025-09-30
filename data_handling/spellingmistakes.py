from textblob import TextBlob
from nltk.corpus import stopwords
import nltk
# sentence_correction
text="helllo certains words are misspelled in englishhg"
def correct_spelling(text):
    text_blob = TextBlob(text)
    corrected_text = text_blob.correct()    
    return str(corrected_text)
#print(correct_spelling(text))     
#stopwords_removel
def remove_stopwords(text):
    new_text=[]
    nltk.download('stopwords')
    for word in text.split():
        if word in stopwords.words('english'):
            new_text.append('')
        else:
            new_text.append(word)
        x=new_text[:]
        new_text.clear()
    return ' '.join(x)
print(remove_stopwords(text))

