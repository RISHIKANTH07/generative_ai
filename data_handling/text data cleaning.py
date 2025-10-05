import pandas as pd
import numpy as np
import re
import string,time
import shortforms
import spellingmistakes as sp
data=pd.read_csv('IMDB Dataset.csv')
df=pd.DataFrame(data)
text="<h1>Welcome to<P> Python <a>Programming</h1>"
data1=shortforms.short_forms
# Convert text to lower case
def lower_case(text):
    data['review']=data['review'].str.lower()
    print(data)
# Remove Punctuation
def removel_htmltags(text):
    clean=re.compile('<.*?>')
    return clean.sub(r'',text)
print(removel_htmltags(text))
data['review']=data['review'].apply(removel_htmltags)
print(data)
# Remove URLS
def  removel_url(text):
    url=re.compile(r'https?://\S+|www\.\S+')
    return url.sub(r'',text)
data['review']=data['review'].apply(removel_url)
print(data)
print(data['review'][10])
#punctuation handling
exclude=string.punctuation
def remove_punctuation(text):
    for char in text:
        if char in exclude:
          text=text=text.replace(char,"")
    return text 
data['review']=data['review'].apply(remove_punctuation)
print(data)
# chat short forms handling
def chat_convertions(text):
    new_text=[]
    for word in text.split():
        if word.lower() in data1:
            new_text.append(data1[word.lower()])
        else:
            new_text.append(word)
    return " ".join(new_text)
print(chat_convertions("i'm idk"))
#textspelling correction
df['review']=df['review'].apply(sp.correct_spelling)
print(df)
#stopwords removal
df['review']=df['review'].apply(sp.remove_stopwords)
print(df)
