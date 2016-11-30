#coding=utf-8  
#!/usr/bin/python  
# Filename : weight.py 

import urllib2
import sys
import re
import time
import os
import shutil
import roe_weight
import revenue_weight
import profit_weight

def main():
	stock_dict = {}

	file_name = './data/stock_data_new'
	stock_data = open(file_name, "rw+")
	stock_dict = eval(stock_data.read())
	stock_data.close()

	# print stock_dict
	# print '\n\n\n'
	# print stock_dict.get('000006')

	DATE_DEMO = stock_dict['000001'][0]
	print 'INFO: Date Sample (000001) : ' + str(DATE_DEMO)

	''' Filter '''
	for key in stock_dict.keys():
		date = stock_dict[key][0]
		if date != DATE_DEMO:
			value = stock_dict.pop(key)
			print 'INFO: Delete Incorrect Date Stock [' + str(key) + ']'

	# print stock_dict

	''' Roe '''
	roe_stock_weight_dict = {}
	roe_stock_weight_dict = roe_weight.get_weight(stock_dict)
	# print roe_stock_weight_dict

	''' Revenue '''
	revenue_stock_weight_dict = {}
	revenue_stock_weight_dict = revenue_weight.get_weight(stock_dict)
	# print revenue_stock_weight_dict

	''' Profit Current Quarter'''
	cur_quarter_profit_stock_weight_dict = {}
	cur_quarter_profit_stock_weight_dict = profit_weight.get_cur_quarter_weight(stock_dict)
	# print cur_quarter_profit_stock_weight_dict

	''' Profit Last Quarter'''
	last_quarter_profit_stock_weight_dict = {}
	last_quarter_profit_stock_weight_dict = profit_weight.get_last_quarter_weight(stock_dict)
	# print last_quarter_profit_stock_weight_dict

	''' Profit Last Year'''
	last_year_profit_stock_weight_dict = {}
	last_year_profit_stock_weight_dict = profit_weight.get_last_year_quarter_weight(stock_dict)
	# print last_year_profit_stock_weight_dict


	''' Output Weight '''
	stock_weight_dict = {}
	for key in stock_dict.keys():
		cur_q_profit = cur_quarter_profit_stock_weight_dict[key]
		last_q_profit = last_quarter_profit_stock_weight_dict[key]
		last_y_profit = last_year_profit_stock_weight_dict[key]
		roe = roe_stock_weight_dict[key]
		revenue = revenue_stock_weight_dict[key]

		profit_total_weight = (cur_q_profit * 40 + last_q_profit * 30 + last_y_profit * 30) / 100
		total_weight = (profit_total_weight * 50 + revenue * 30 + roe * 20) / 100
		stock_weight_dict[key] = total_weight


	''' Save To File '''
	file_name = './data/stock_weight_' + time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
	stock_weight = open(file_name, "w+")

	weight_list = sorted(stock_weight_dict.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
	for item in weight_list:
		temp = str(item[0]) + '		' + str(item[1]) + '\n'
		stock_weight.write(temp)
	stock_weight.close()
	print 'INFO: New Stock File [' + file_name + ']'

	file_name_new = './data/stock_weight_new'
	if os.path.isfile(file_name_new):
	    print 'INFO: Delete File [' + file_name_new + ']'
	    os.remove(file_name_new)
	    time.sleep(2)

	print 'INFO: Copy File From [' + file_name + '] To [' + file_name_new + ']'
	shutil.copy(file_name, file_name_new)

	print '******************************************************'
	print ' SUCCESS '
	print '******************************************************'
	print ' Output File Path : ' + file_name_new
	print '******************************************************'
	print ' Completed'
	print '******************************************************'

