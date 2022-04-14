import pandas as pd
import argparse
import tqdm
import traceback
import itertools
parser = argparse.ArgumentParser()
parser.add_argument("--file", help = 'Filename')



args = parser.parse_args()
df = pd.read_csv(args.file)
data = df['key'].values.tolist()
data = itertools.chain(*data)
print(data[0])
print(data10])
