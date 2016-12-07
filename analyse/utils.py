# coding=utf-8
# !/usr/bin/python
# Filename : utils.py 

import urllib2
import sys
import re
import time

# change formmat from str to float, and remove comma character
# '1,567.72' ---> 1567.72 
def strToFloat(str):
    if str is None:
        print 'Error: strToNum, str is null'

    number = 0.0

    if '--' in str:
        number = 0.0
    else:
        string = str.replace(",", "")
        number = float(string)

    return number

# (100亿，100万，10，--) to float
def strBigToFloat(str):
    if str is None:
        print 'Error: strBigToFloat, str is null'

    num = 0.0

    if '--' in str:
        num = 0.0
    elif '万' in str:
        num = float(str.replace('万', '')) * 10000
    elif '亿' in str:
        num = float(str.replace('亿', '')) * 100000000
    else:
        num = float(str)
        
    return num