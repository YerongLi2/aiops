import pandas as pd
from fastai.text.all import *
from transformers import *
from blurr.data.all import *
from blurr.modeling.all import *

#Get data
df = pd.read_csv('articles.csv', error_bad_lines=False, sep=';')
df = df.dropna().reset_index()

#Select part of data we want to keep
df = df[(df['language']=='english') & (df['type']=='bs')].reset_index()
df = df[['title','text']]

#Clean text
df['text'] = df['text'].apply(lambda x: x.replace('\n',''))

#Select only part of it (makes testing faster)
articles = df.head(100)
articles.head()