import pandas as pd
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--file", 'Filename')
args = parser.parse_args()
print('args.file', args.file)
df = pd.read_csv(args.file)