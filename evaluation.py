

# import collections
# import re
# from d2l import torch as d2l


# d2l.DATA_HUB['nvidia'] = (d2l.DATA_URL + 'nvidia.txt',
#                                 '090b5e7e70c295757f55df93cb0a180b9691891a')

# def read_time_machine():  
#     """Load the time nvidia dataset into a list of text lines."""
#     with open(d2l.download('time_machine'), 'r') as f:
#         lines = f.readlines()
#     return [re.sub('[^A-Za-z]+', ' ', line).strip().lower() for line in lines]

# lines = read_time_machine()
# print(f'
# print(lines[0])
from os import linesep


fdup = open('duplicates.txt', 'r')
for line in fdup:
    if len(line.split(',')) == 2:

        print(line)