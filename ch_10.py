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
