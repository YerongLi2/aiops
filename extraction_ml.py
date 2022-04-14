from monkeylearn import MonkeyLearn
import pandas as pd
import argparse
import tqdm
import traceback
from itertools import chain
parser = argparse.ArgumentParser()
parser.add_argument("--file", help = 'Filename')


ml = MonkeyLearn('7cfbdb347b316cb465185868e4ec75e145ddb7b4')
model_id = 'ex_YCya9nrn'

args = parser.parse_args()
df = pd.read_csv(args.file)
if 'Unnamed: 0' in df.columns: df.drop('Unnamed: 0', 1, inplace=True)

if 'key' not in df.columns:
    df['key'] = ['0']*df.shape[0]

try:
    for i in tqdm.tqdm(range(df.shape[0])):
        if df.iloc[i]['key'] != 0: continue
        posts = eval(df.iloc[i]['posts'])
        for j in range(len(posts)):
            data = [posts[j][0]]
            result = ml.extractors.extract(model_id, data)
            keywords = [item ['parsed_value'] for item in result.body[0]['extractions']]
            posts[j][0] = keywords
            
            df.at[i, 'key'] = str(posts)
        
        raise NotImplemented
except:
    traceback.print_exc()
    df.to_csv(args.file, index = False)
    print('Saved to ' + args.file)