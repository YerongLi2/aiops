import pandas as pd
import argparse
import tqdm
import traceback
from itertools import chain
parser = argparse.ArgumentParser()
parser.add_argument("--file", help = 'Filename')



args = parser.parse_args()
df = pd.read_csv(args.file)
print(df.iloc[1]['key'])
keywords = [post[0] for post in eval(df.iloc[1]['key'])]
print(keywords)