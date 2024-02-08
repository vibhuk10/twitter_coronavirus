#!/usr/bin/env python3

# Arguments
import argparse
parser = argparse.ArgumentParser()
#parser.add_argument('--input_paths',nargs='+',required=True)
parser.add_argument('--keys',nargs='+',required=True)
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime
import glob

# load each of the input paths
total = {key: [] for key in args.keys}
paths = glob.glob('outputs/geoTwitter*.lang')
for path in paths:
    date = os.path.splitext(os.path.basename(path))[0][10:18]
    with open(path) as f:
        tmp = json.load(f)
        for k in tmp:
            print(args.keys)
            if k in args.keys:
                counts = 0
                for key in tmp[k]:
                    counts += tmp[k][key]
                print(counts)
                total[k].append((date, counts))
print(total)
# make the plot
