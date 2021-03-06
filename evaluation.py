

# import collections
# import re
# from d2l import torch as d2l


# d2l.DATA_HUB['nvidia'] = (d2l.DATA_URL + 'nvidia.txt',
#                                 '090b5e7e70c295757f55df93cb0a180b9691891a')

# def read_time_machine():  
#     """Load the time nvidia dataset into a list of text lines."""
#     with open(d2l.download('time_machine'), 'r') as f:
#         lines = f.readlines()
#     return [re.sub('[^A-Za-z]+', ' ', line).strip().lower() for line in lines]

# lines = read_time_machine()
# print(f'
# print(lines[0])
from os import linesep, pread
import pandas as pd
df = None
filenames = ['drive-px2.csv.1', 'drive-agx.csv.1']
for filename in filenames:
    if df is None:
        df = pd.read_csv(filename)
    else:
        df = pd.concat([df, pd.read_csv(filename)], ignore_index=True)
df.url = df.url.apply(lambda x : "/".join(x.split('/')[:6]))
df.drop_duplicates(['url'], inplace=True, ignore_index=True)
print(df.shape)
fdup = open('duplicates.txt', 'r')


for line in fdup:
    if len(line.split(',')) == 2:
        new, old = line.split(',')
        # if 0 == len(df.get(df['url']==new).key.values.tolist()) :
        if 0 == len(df.get(df['url']==old).key.values.tolist()) :
            print(old)
        # new_posts = df.get(df['url']==new).key.values.tolist()[0]
        # old_posts = df.get(df['url']==old).key.values.tolist()[0]
        # print(new_posts)
        # print(old_posts)