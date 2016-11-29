#coding=utf-8  
#!/usr/bin/python  
# Filename : revenue_weight.py 

import urllib2
import sys
import re
import time
import utils

def get_weight(stock_dict):
	stock_weight_dict = {}

	# key : roe_value, value : roe_weght
	value_weight_dict = {}
	revenue_list = []

	for key in stock_dict.keys():
		str_v = stock_dict[key][2][0]
		# print str(key) + '	' + str(v)
		fla_v = utils.strToFloat(str_v)
		revenue_list.append(fla_v)

	revenue_list = list(set(revenue_list))
	revenue_list.sort()
	total = len(revenue_list)

	for item in revenue_list:
		item_index = revenue_list.index(item) + 1
		item_weight = float(100) * item_index / total
		item_weight = round(item_weight, 5)
		value_weight_dict[item] = item_weight

	for key, value in stock_dict.items():
		fla_v = utils.strToFloat(value[2][0])
		weight = value_weight_dict[fla_v]
		stock_weight_dict[key] = weight
		# print str(key) + '		' + str(fla_v) + '		' + str(weight)

	return stock_weight_dict