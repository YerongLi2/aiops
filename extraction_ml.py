from monkeylearn import MonkeyLearn
import pandas as pd
import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument("--file", help = 'Filename')


ml = MonkeyLearn('7cfbdb347b316cb465185868e4ec75e145ddb7b4')
data = []
model_id = 'ex_YCya9nrn'

args = parser.parse_args()
df = pd.read_csv(args.file)

print(df.shape)
if 'key' not in df.columns:
    df['key'] = ['']*df.shape[0]

for i in range(df.shape[0]):
    print(df.iloc[i]['post'])
    sys.exit()
    # result = ml.extractors.extract(model_id, data)
    # print(result.body)