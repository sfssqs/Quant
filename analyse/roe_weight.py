#coding=utf-8  
#!/usr/bin/python  
# Filename : roe_weight.py 

import urllib2
import sys
import re
import time

def get_weight(stock_dict):
	stock_weight_dict = {}

	# key : roe_value, value : roe_weght
	value_weight_dict = {}
	roe_list = []

	for key in stock_dict.keys():
		roe_value = float(stock_dict[key][3])
		roe_list.append(roe_value)

	roe_list = list(set(roe_list))
	roe_list.sort()
	total = len(roe_list)

	for item in roe_list:
		item_index = roe_list.index(item) + 1
		item_weight = float(100) * item_index / total
		item_weight = round(item_weight, 5)
		value_weight_dict[item] = item_weight

	for key, value in stock_dict.items():
		value = float(value[3])
		weight = value_weight_dict[value]
		stock_weight_dict[key] = weight
		# print str(key) + '		' + str(value) + '		' + str(weight)

	return stock_weight_dict