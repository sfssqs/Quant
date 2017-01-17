#coding=utf-8  
#!/usr/bin/python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

RESISTANCE_FACTOR = 0.3

def _filter(data):
    filter_data = data.loc[:, ['open', 'high', 'close','low']]
    filter_data['price_change'] = filter_data.close - filter_data.open
    return filter_data

def _resistance(data):
    fall_data = data[data.price_change < 0]
    print fall_data
    print '================================================='

    for index, row in fall_data.iterrows():
        ref_data = data[:index].drop([index], axis=0)
        result = _calculate_single_resistance(row, ref_data)
        print '[' + str(index) + '] ' + str(result)

def _calculate_single_resistance(single_data, data):
    factor_value = abs(single_data.price_change) * RESISTANCE_FACTOR
    ref_price = single_data.close + round(factor_value, 2)
    for index, row in data.iterrows():
        if row.high > ref_price:        
            return False

    return True

def _support(data):
    rise_data = data[data.price_change > 0]
    print rise_data
    print '================================================='

    for index, row in rise_data.iterrows():
        ref_data = data[:index].drop([index], axis=0)
        result = _calculate_single_support(row, ref_data)
        print '[' + str(index) + '] ' + str(result)

def _calculate_single_support(single_data, data):
    factor_value = abs(single_data.price_change) * RESISTANCE_FACTOR
    ref_price = single_data.close - round(factor_value, 2)
    for index, row in data.iterrows():
        if row.low < ref_price:        
            return False

    return True


df = pd.read_csv('../price/data/600035.csv', index_col='date')
dfhead = df['2016-11-28':'2016-11-10']
# dfhead = df.head(500)
filter_data = _filter(dfhead)

print filter_data
print '================================================='
# _resistance(filter_data)
# print '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
_support(filter_data)


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


	