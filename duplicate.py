import pandas as pd
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--file", help = 'Filename')
args = parser.parse_args()
df = pd.read_csv(args.file)
df.url = df.url.apply(lambda x : "/".join(x.split('/')[:6]))
df.drop_duplicates(['url'], inplace=True)
url = df.url[0]
print(url)
url = df.url[1]
# print(url)