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
