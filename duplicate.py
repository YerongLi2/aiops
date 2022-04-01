import pandas as pd
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--file", help = 'Filename')
args = parser.parse_args()
df = pd.read_csv(args.file)
df.url = df.url.apply(lambda x : "/".join(x.split('/')[:6]))
df.drop_duplicates(['url'], inplace=True, ignore_index=True)
print(df.columns)
print('Unnamed: 0' in df.columns)
# if 'Unnamed: 0' in df.columns: df.drop('Unnamed: 0', inplace=True)
df.to_csv(args.file,index=False)