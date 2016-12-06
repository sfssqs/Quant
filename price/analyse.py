import pandas as pd
import tushare as ts
import datetime
import time
import os
import shutil
import StringIO

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

	for key, value in price_dict.items():
		print str(key) + ' ' + str(value)