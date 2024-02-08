#!/usr/bin/env python3

# Arguments
import argparse

def list_of_strings(arg):
    return arg.split(',')

parser = argparse.ArgumentParser()
#parser.add_argument('--input_paths',nargs='+',required=True)
parser.add_argument('--keys',nargs='+', type=list_of_strings)
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

print(args.keys[0])
# load each of the input paths
total = {key: [] for key in args.keys[0]}
paths = glob.glob('outputs/geoTwitter*.lang')
for path in paths:
    date = os.path.splitext(os.path.basename(path))[0][10:18]
    with open(path) as f:
        tmp = json.load(f)
        for k in tmp:
            if k in args.keys[0]:
                counts = 0
                for key in tmp[k]:
                    counts += tmp[k][key]
                total[k].append((date, counts))
print(total)

# make the plot
for hashtag, date_count_pairs in total.items():
    dates, counts = zip(*[(datetime.strptime(date, '%y-%m-%d'), count) for date, count in date_count_pairs])

    # Sorting data based on dates
    sorted_indices = sorted(range(len(dates)), key=lambda k: dates[k])
    dates = [dates[i] for i in sorted_indices]
    counts = [counts[i] for i in sorted_indices]

    # Plotting
    plt.plot(dates, counts, label=hashtag)

# Formatting the plot
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('Hashtag Count Over Time')
plt.legend()
name = [] 
for a in args.keys[0]:
    name.append(a[1:])
final_name = '_'.join(name)
plt.savefig(final_name + '.png')

