import pandas as pd
import tushare as ts
import datetime
import time
import os
import shutil
import StringIO
import tools

date_base = datetime.date.today()
global date_base

def filter_none(data, num):
	if data is None:
		return 0.0
	else:
		return round(data, num)

def get_rate(new, old):
	if  new  is None or old is None:
		return 0.0
	else:
		return 100 * (new - old) / old		

def getPricebyData(date, df):
	global date_base
	days = (date_base - date).days

	if days > 365:
		return None

	try:
		price = df.loc[str(date), 'close']
		print 'INFO: Successful, Date = ' + str(date)
	except Exception, e:
		temp_date = date - datetime.timedelta(days=1)
		return getPricebyData(temp_date, df)

	return price

def getPrice(date, df):
	price = getPricebyData(date, df)
	return price

def getPriceArray(stock, date, df):
	total_array = []
	price_array = []
	rate_array = []

	q1  = date
	q2 = q1 - datetime.timedelta(days=91)
	q3 = q2 - datetime.timedelta(days=91)
	q4 = q3 - datetime.timedelta(days=91)
	q5= q4 - datetime.timedelta(days=91)

	q1_price = 0.0
	q2_price = 0.0
	q3_price = 0.0
	q4_price = 0.0
	q5_price = 0.0

	q1_price =  getPrice(q1, df)
	q2_price =  getPrice(q2, df)
	q3_price =  getPrice(q3, df)
	q4_price =  getPrice(q4, df)
	q5_price =  getPrice(q5, df)

	if q4_price  is None:
		print 'WARNING: '  + stock + ' ' + str(q1_price) + ' ' + str(q2_price) + ' ' + str(q3_price) + ' ' + str(q4_price) + ' ' + str(q5_price)

	q1_rate = 0.0
	q2_rate = 0.0
	q3_rate = 0.0
	q4_rate = 0.0

	q1_rate = get_rate(q1_price, q2_price)
	q2_rate = get_rate(q2_price, q3_price)
	q3_rate = get_rate(q3_price, q4_price)
	q4_rate = get_rate(q4_price, q5_price)

	price_array.append(filter_none(q1_price, 2))
	price_array.append(filter_none(q2_price, 2))
	price_array.append(filter_none(q3_price, 2))
	price_array.append(filter_none(q4_price, 2))	
	price_array.append(filter_none(q5_price, 2))		

	rate_array.append(round(q1_rate, 2))
	rate_array.append(round(q2_rate, 2))
	rate_array.append(round(q3_rate, 2))
	rate_array.append(round(q4_rate, 2))

	total_array.append(rate_array)
	total_array.append(price_array)

	return total_array

if __name__ == '__main__':
	price_dict = {}

	line = [line.rstrip() for line in open('../data/stock_list')]
	for item in line:
		file_name = 'data/' + item + '.csv'
		if os.path.exists(file_name):			
			df = pd.read_csv(file_name, index_col=0)
			price_array = getPriceArray(item, date_base, df)
			price_dict[item] = price_array 
		else:
			print 'ERROR: ' + str(file_name) + ' is not exist!'

	total_dict = {}
	
	q1_dict = {}
	q2_dict = {}
	q3_dict = {}
	q4_dict = {}

	for key, value in price_dict.items():
		q1_dict[key] = value[0][0]
		q2_dict[key] = value[0][1]
		q3_dict[key] = value[0][2]
		q4_dict[key] = value[0][3]

	q1_weight = tools.get_weight(q1_dict)
	q2_weight = tools.get_weight(q2_dict)
	q3_weight = tools.get_weight(q3_dict)
	q4_weight = tools.get_weight(q4_dict)

	for key, value in price_dict.items():
		print '---------------------------------------------------------------------'
		# print key + '	' + str(value)
		# print key + '	' + str(q1_dict[key]) + '	' + str(q1_weight[key])
		# print key + '	' + str(q2_dict[key]) + '	' + str(q2_weight[key])
		# print key + '	' + str(q3_dict[key]) + '	' + str(q3_weight[key])
		# print key + '	' + str(q4_dict[key]) + '	' + str(q4_weight[key])

		final_weight = (q1_weight[key] * 40 + q2_weight[key] * 20 + q3_weight[key] * 20 + q4_weight[key] * 20) / 100
		final_weight = round(final_weight, 5)

		total_list = []
		

		weight_list = []
		weight_list.append(q1_weight[key])
		weight_list.append(q2_weight[key])
		weight_list.append(q3_weight[key])
		weight_list.append(q4_weight[key])

		price = value[1]
		rate = value[0]

		total_list.append(final_weight)
		total_list.append(weight_list)
		total_list.append(rate)
		total_list.append(price)
		
		# print key + '	' + str(value)
		print key + '	' + str(total_list)

		total_dict[key] = total_list

		# time.sleep(1)

	print '=========================================================================='
	weight_list = sorted(total_dict.items(), lambda x, y: cmp(x[1][0], y[1][0]), reverse=True)
	for item in weight_list:
		temp = str(item[0]) + '		' + str(item[1]) + '\n'
		print str(item[0]) + '		' + str(item[1])






