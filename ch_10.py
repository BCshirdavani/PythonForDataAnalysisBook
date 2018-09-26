#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 23:11:56 2018

@author: shimac
"""

#   Time Series
#   Chapter 10

# pp.286 ***************************************************************
# Date and Time Data Types and Tools
from datetime import datetime
now = datetime.now()
now
print(now)
now.year, now.month, now.day

#   temporal difference between 2 datetime objects
delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
delta   
delta.days
delta.seconds
#   add or subtract timedelta, or miltiple therof
from datetime import timedelta
start = datetime(2011, 1, 7)
start + timedelta(12)
start - 2 * timedelta(12)

#   converting between string and datetime
#       datetime -> string
stamp = datetime(2011, 1, 3)
str(stamp)
stamp.strftime('%Y-%m-%d')
#       string -> datetime
value = '2011-01-03'
datetime.strptime(value, '%Y-%m-%d')
datestrs = ['7/6/2011', '8/6/2011']
[datetime.strptime(x, '%m/%d/%Y') for x in datestrs]

#   use dateutil package perser, to avoid retyping the date format
#   this parser will auto parse almost any date format
from dateutil.parser import parse
parse('2011-01-03')
parse('Jan 31, 1997 10:45 PM')
#   international locals, with day before month...
parse('6/12/2011', dayfirst = True)

#   converting to datetime using pandas
import pandas as pd
datestrs
pd.to_datetime(datestrs)
idx = pd.to_datetime(datestrs + [None])
idx[2]
idx[1]
pd.isnull(idx)

# pp.289 ***************************************************************
# Time Series Basics
from datetime import datetime
import numpy as np
dates = [datetime(2011,1,2), datetime(2011,1,5), datetime(2011,1,7), datetime(2011,1,8), datetime(2011,1,10), datetime(2011,1,12)]
ts = pd.Series(np.random.randn(6), index = dates)
ts
ts.index
ts + ts[::2]
ts.index.dtype
stamp = ts.index[0]
stamp

# pp.290 ***************************************************************
# Indexing, Selection, Subsetting
stamp = ts.index[2]
print(stamp)
ts[stamp]
#   passing a string that is interpretable as a date for the index
ts['1/10/2011']
#   makoing a longer time series
longer_ts = pd.Series(np.random.rand(1000), index=pd.date_range('1/1/2000', periods=1000))
longer_ts
#       select slices based on year only
longer_ts['2001']
#       select slices based on year + month
longer_ts['2001-05']
#       slicingg using typical series index format, but with dates
ts[datetime(2011,1,7):]
#       range query, using dates that aren't explicitly in the series
ts
ts['1/6/2011':'1/11/2011']
#       range query, using truncate method
ts.truncate(after='1/9/2011')
#   doing similar indexing on date ranges, for data frames now
dates = pd.date_range('1/1/2000', periods=100, freq='W-WED')
long_df = pd.DataFrame(np.random.randn(100,4), index = dates, columns = ['Colorado', 'Texas', 'New York', 'Ohio'])
long_df.ix['5-2001']


# pp.292 ***************************************************************
# Time Series with Duplicate Indices







