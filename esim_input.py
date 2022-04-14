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
    print(len(df['key'].values.tolist()))
    data = [eval(item) for item in df['key'].values.tolist()]
    data = [item for item in data if item != 0]
    data = list(itertools.chain(*data))
    data = [item[0] for item in data]
    data = list(itertools.chain(*data))

    print(len(set(data)))
    # print(data[0])
    # print(data[1])
