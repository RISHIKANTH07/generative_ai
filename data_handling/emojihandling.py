import pandas as pd
import re   
import emoji
data=pd.read_csv('IMDB Dataset.csv')
df=pd.DataFrame(data)
def remove_emoji(text):
    emoji_pattern=re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+",flags=re.UNICODE)
    return emoji_pattern.sub(r'',text)
df['review']=df['review'].apply(remove_emoji)
print(df)
text1="Hello😊"
def demojize_text(text1):
    return emoji.demojize(text1)
df['review']=df['review'].apply(demojize_text)
print(df)