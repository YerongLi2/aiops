import pandas as pd
import argparse
import tqdm
import traceback
import itertools
parser = argparse.ArgumentParser()
parser.add_argument("--file", help = 'Filename')

filenames = ['drive-px2.csv.1', 'drive-agx.csv.1']

args = parser.parse_args()
# df = pd.read_csv(args.file)
for filename in filenames:
    df = pd.read_csv(filename)
    print(len(df['key'].values))
    # data = [eval(item) for item in ].tolist()
    data = list(itertools.chain(*data))
    print(data[0])
    print(data[1])
