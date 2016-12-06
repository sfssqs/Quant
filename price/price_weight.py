#coding=utf-8  
#!/usr/bin/python  
# Filename : price_weight.py 

import urllib2
import sys
import re
import time
import utils

def get_q1_weight(stock_dict):
	stock_weight_dict = {}
	stock_value_dict = {}
	value_weight_dict = {}
	profit_list = []

	for key in stock_dict.keys():
		profit_array = stock_dict[key][1]
		a1 = utils.strBigToFloat(profit_array[0])
		a2 = utils.strBigToFloat(profit_array[4])
		if a2 == 0:
			value = 100.0
		else:
			value = float(100 * (a1 - a2) / abs(a2))
			value = round(value, 5)

		stock_value_dict[key] = value
		profit_list.append(value)

	profit_list = list(set(profit_list))
	profit_list.sort()
	total = len(profit_list)

	for item in profit_list:
		item_index = profit_list.index(item) + 1
		item_weight = float(100) * item_index / total
		item_weight = round(item_weight, 5)
		value_weight_dict[item] = item_weight

	for key, value in stock_value_dict.items():
		weight = value_weight_dict[value]
		stock_weight_dict[key] = weight
		# print str(key) + '		' + str(value) + '		' + str(weight)

	return stock_weight_dict

def get_last_quarter_weight(stock_dict):
	stock_weight_dict = {}
	stock_value_dict = {}
	value_weight_dict = {}
	profit_list = []

	for key in stock_dict.keys():
		profit_array = stock_dict[key][1]
		a1 = utils.strBigToFloat(profit_array[1])
		a2 = utils.strBigToFloat(profit_array[5])
		if a2 == 0:
			value = 100.0
		else:
			value = float(100 * (a1 - a2) / abs(a2))
			value = round(value, 5)

		stock_value_dict[key] = value
		profit_list.append(value)

	profit_list = list(set(profit_list))
	profit_list.sort()
	total = len(profit_list)

	for item in profit_list:
		item_index = profit_list.index(item) + 1
		item_weight = float(100) * item_index / total
		item_weight = round(item_weight, 5)
		value_weight_dict[item] = item_weight

	for key, value in stock_value_dict.items():
		weight = value_weight_dict[value]
		stock_weight_dict[key] = weight
		# print str(key) + '		' + str(value) + '		' + str(weight)

	return stock_weight_dict

def get_last_year_quarter_weight(stock_dict):
	stock_weight_dict = {}
	stock_value_dict = {}
	value_weight_dict = {}
	profit_list = []

	for key in stock_dict.keys():
		profit_array = stock_dict[key][4]
		a1 = utils.strBigToFloat(profit_array[0])
		a2 = utils.strBigToFloat(profit_array[1])
		
		if a2 == 0:
			value = 100.0
		else:
			value = 100 * float((a1 - a2) / abs(a2))
			value = round(value, 5)

		stock_value_dict[key] = value
		profit_list.append(value)

	profit_list = list(set(profit_list))
	profit_list.sort()
	total = len(profit_list)

	for item in profit_list:
		item_index = profit_list.index(item) + 1
		item_weight = float(100) * item_index / total
		item_weight = round(item_weight, 5)
		value_weight_dict[item] = item_weight

	for key, value in stock_value_dict.items():
		weight = value_weight_dict[value]
		stock_weight_dict[key] = weight
		# print str(key) + '		' + str(value) + '		' + str(weight)

	return stock_weight_dict