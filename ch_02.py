#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created:    Mon Sep 24 18:23:08 2018
@author:    shimac
Title:      Python For Data Analysis - practice
            Chapter 2

"""

#   pp.14 ******************************************************************
path = '/Users/shimac/Documents/PythonBooks/PythonForData_bigDataSets/usagov_bitly_data2012-03-16-1331923249.txt'
open(path).readline()
import json
path = '/Users/shimac/Documents/PythonBooks/PythonForData_bigDataSets/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path, 'rb')]
records[0]
print("records[0]:\n\t", records[0])
records[0]['tz']
print("records[0]['tz':\n\t", records[0]['tz'])

#   pp.15 - counting time zones ********************************************
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
time_zones[:10]
#       counting manually with dictionaries
def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

manualCounts = get_counts(time_zones)
print(manualCounts)

#       similar method, but with defaultdict library
from collections import defaultdict
def get_counts2(sequence):
    counts = defaultdict(int) # values will initialize to 0
    for x in sequence:
        counts[x] += 1
    return counts
manualCounts2 = get_counts2(time_zones)

#       show the top 10 counted time zones from the dicts we made
def top_counts(count_dict, n = 10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

top_counts(manualCounts)

#       count using the collections.Counter class
from collections import Counter
counts = Counter(time_zones)
counts.most_common(10)

#   pp.17 - counting time zones with pandas  ********************************
from pandas import DataFrame, Series
import pandas as pd
frame = DataFrame(records)
frame.info()
frame['tz'][:10]
tz_counts = frame['tz'].value_counts()
tz_counts[:10]
#       clean the missing data
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
tz_counts[:10]
#       plotting the data we now cleaned
frame['a'][1]
frame['a'][50]
frame['a'][51]
tz_counts[:10].plot(kind = 'barh', rot = 0)
#      parsing the strings 
results = Series([x.split()[0] for x in frame.a.dropna()])
results[:5]
results.value_counts()[:8]
#   pp.20 ******************************************************************