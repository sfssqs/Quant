#coding=utf-8  
#!/usr/bin/python

import sys
sys.path.append("..")

import tushare as ts
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

from enum import Enum
from utils import logger as log

RESISTANCE_FACTOR = 0.3
logger = log.Logger()

class FilterType(Enum):
    local = 1
    server = 2

def _normalize(data, type):
    if type == FilterType.local:
        filter_data = data.loc[:, ['open', 'high', 'close','low']]
        filter_data['price_change'] = filter_data.close - filter_data.open
        return filter_data
    elif type == FilterType.server:
        filter_data = data.loc[:, ['date', 'open', 'high', 'close','low']]
        filter_data['price_change'] = filter_data.close - filter_data.open
        filter_data = filter_data.set_index(['date'])
        return filter_data

def _resistance(data):
    fall_data = data[data.price_change <= 0]
    for index, row in fall_data.iterrows():
        ref_data = data[:index].drop([index], axis=0)
        result = _calculate_single_resistance(row, ref_data)
        logger.info('[' + str(index) + '] ' + str(result))

def _calculate_single_resistance(single_data, data):
    factor_value = abs(single_data.price_change) * RESISTANCE_FACTOR
    ref_price = single_data.close + round(factor_value, 2)
    for index, row in data.iterrows():
        if row.high > ref_price:        
            return False

    return True

def _support(data):
    rise_data = data[data.price_change >= 0]
    for index, row in rise_data.iterrows():
        ref_data = data[:index].drop([index], axis=0)
        result = _calculate_single_support(row, ref_data)
        logger.info('[' + str(index) + '] ' + str(result))

def _calculate_single_support(single_data, data):
    factor_value = abs(single_data.price_change) * RESISTANCE_FACTOR
    ref_price = single_data.close - round(factor_value, 2)
    for index, row in data.iterrows():
        if row.low < ref_price:
            return False

    return True

'''
    注意：
    目前程序默认需要从现在到过去的排序
    get_k_data: 获取到的数据从过去到现在排序
    get_h_data: 获取到的数据从现在到过去排序

    -------------------------------------

    param: stockId, 600035
    param: period, 'D', 'W', 'M', 'Q', 'Y'
    param: start, 2016-10-10
    param: end, 2017-10-10
'''
def _fetch_source_data(stockId):
    df = ts.get_k_data(stockId, start='2016-07-06', end='2017-01-17', ktype='W', autype='qfq')
    # dfhead = df['2016-11-28':'2016-11-10']
    dfhead = df
    normalize_data = _normalize(dfhead, FilterType.server)
    reverse_data = normalize_data.reindex(index=normalize_data.index[::-1]).copy()
    
    logger.info('resistance')
    logger.info('-----------------------------')
    _resistance(reverse_data)
    logger.info('=============================')
    logger.info('support')
    logger.info('-----------------------------')
    _support(reverse_data)

_fetch_source_data('000043')



##########################################################################
# df = ts.get_h_data('000043', start='2017-01-16', ktype='W')
# df = pd.read_csv('../price/data/600035.csv', index_col='date')
# dfhead = df['2016-11-28':'2016-11-10']
# # dfhead = df.head(500)
# filter_data = _normalize(dfhead, FilterType.local)

# print filter_data
# print '================================================='
# _resistance(filter_data)
# print '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
# _support(filter_data)

##########################################################################
# 截取数据，最新50周
# head50 = df.head(5)
# print head50
# print 'head50 data print over'

# head50 = head50.loc[:, ['date', 'open', 'high', 'close','low']]
# print head50

# head50['price_change'] = head50.close - head50.open
# print head50

# for index, row in fall_data.iterrows():
#     print 'index : ' + str(index)
#     ref_data = data[:index]
#     result = _calculate_single_resistance(row, ref_data)
#     print result
#     print '-------------------------------'
#     time.sleep(1)


# 1. 删除索引，重新建立索引
# def test4():  
#     obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])  
#     print obj3  
#     obj4 = obj3.reset_index(drop=True)  
#     print obj4  
#     print type(obj4)  

# 2. 删除行需要重新复制给新变量
# ref_data = data[:index].drop([index], axis=0)


# 3. 通过索引进行迭代
# for index in range(0, fall_data.shape[0]):
#     date = fall_data.index
#     row = fall_data.loc[date[index]]
#     ref_data = data.loc[:date[index]]
#     # ref_data.drop([row.index], axis=0)
#     print index
#     print row
#     print ref_data
#     print '--------------------------------------'
#     result = _calculate_single_resistance(row, ref_data)


	