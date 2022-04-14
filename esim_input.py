import pandas as pd
import argparse
import tqdm
import traceback
import itertools
import os
parser = argparse.ArgumentParser()
parser.add_argument("--file", help = 'Filename')

filenames = ['drive-px2.csv.1', 'drive-agx.csv.1']

args = parser.parse_args()
# df = pd.read_csv(args.file)
directory = 'nvidia'
try:
    os.stat(directory)
except:
    os.mkdir(directory)
fnode = open(directory + '/node.dat'  , "w")
flink = open(directory + '/link.dat'  , "w")
for filename in filenames:
    topic = filename[:-6]
    fnode.write('t ' + topic + '\n')
    df = pd.read_csv(filename)
    print(len(df['key'].values.tolist()))
    data = [eval(item) for item in df['key'].values.tolist()]
    data = [item for item in data if item != 0]
    data = list(itertools.chain(*data))
    data = [item[0] for item in data]
    data = sorted(list(set(list(itertools.chain(*data)))))
    data = [item.replace(' ','-') for item in data]
    for item in data:
        flink.write(topic + ' ' + item + '\n')
        fnode.write('w ' + item + '\n')
        
fnode.close()
flink.close()
