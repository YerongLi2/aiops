from monkeylearn import MonkeyLearn
import pandas as pd
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--file", help = 'Filename')


ml = MonkeyLearn('7cfbdb347b316cb465185868e4ec75e145ddb7b4')
data = []
model_id = 'ex_YCya9nrn'

args = parser.parse_args()
df = pd.read_csv(args.file)

if 'key' not in df.columns:
    df['key'] = [[]*df.shape[0]]

    result = ml.extractors.extract(model_id, data)
    print(result.body)