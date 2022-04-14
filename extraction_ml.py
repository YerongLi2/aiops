from monkeylearn import MonkeyLearn
import pandas as pd
import argparse
import tqdm
import traceback
from itertools import chain
parser = argparse.ArgumentParser()
parser.add_argument("--file", help = 'Filename')


# ml = MonkeyLearn('7cfbdb347b316cb465185868e4ec75e145ddb7b4') # yerongli.ads
# ml = MonkeyLearn('2fdd3e3c7aad8699d5ebb6f54c7b445e1f19b0a6') # yerongli.shop1
ml = MonkeyLearn('b63939e6d125a3dd15a4774db5c3a59d02d90d65') # yerongli.shop2
model_id = 'ex_YCya9nrn'

args = parser.parse_args()
df = pd.read_csv(args.file)
if 'Unnamed: 0' in df.columns: df.drop('Unnamed: 0', 1, inplace=True)

if 'key' not in df.columns:
    df['key'] = ['0']*df.shape[0]
alldata = df.values.tolist()
try:
    for i in tqdm.tqdm(range(df.shape[0])):
        if df.iloc[i]['key'] != '0' and df.iloc[i]['key'] != 0: 
            print(f'skipped {i}')
            continue
        posts = eval(df.iloc[i]['posts'])
        for j in range(len(posts)):
            try :
                data = [posts[j][0]]
                result = ml.extractors.extract(model_id, data)
                # print('result.body')
                # print(result.body)
                keywords = [] if result.body[0]['extractions'] is None else [item ['parsed_value'] for item in result.body[0]['extractions']]
                posts[j][0] = keywords
            except:
                traceback.print_exc()
                posts = '0'
        alldata[i][2] = str(posts)
        if posts == '0': raise NotImplemented
        # raise NotImplemented
except:
    traceback.print_exc()
    df = pd.DataFrame(columns=df.columns, data = alldata)
    df.to_csv(args.file, index = False)
    print('Saved to ' + args.file)