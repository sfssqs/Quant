#coding=utf-8  
#!/usr/bin/python  
# FileName : weight.py 

import urllib2
import sys
import re
import time

'''

@ Param dict(key, value)
@ Return: dict(key, weight)

'''

def get_weight(key_value_dict):

	key_weight_dict = {}
	value_weight_dict = {}
	value_list = []

	for key in key_value_dict.keys():
		value = key_value_dict[key]
		value_list.append(value)

	value_list = list(set(value_list))
	value_list.sort()
	value_list_len = len(value_list)

	for item in value_list:
		item_index = value_list.index(item) + 1
		item_weight = float(100) * item_index / value_list_len
		item_weight = round(item_weight, 5)
		value_weight_dict[item] = item_weight

	for key, value in key_value_dict.items():
		weight = value_weight_dict[value]
		key_weight_dict[key] = weight

	return key_weight_dict



if __name__ == '__main__':
	demo_dict = {}
	demo_dict['01'] = [11, 12, 13]
	demo_dict['02'] = [21, 22, 23]
	demo_dict['03'] = [31, 32, 33]

	print demo_dict
	print '-------------------------------------'

	temp_dict = {}
	for key, value in demo_dict.items():
		temp_dict[key] = value[0]

	print temp_dict
	print '-------------------------------------'
	print get_weight(temp_dict)
	print '-------------------------------------'