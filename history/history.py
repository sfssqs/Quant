import pandas as pd
import tushare as ts
import datetime
import time

def get_h_data(stock_code, day):
	for index in range(3):
		df = ts.get_h_data(stock_code, start=str(day), end=str(day))
		if df is not None:
			break
		else:
			print 'sleep'
			time.sleep(2)

	return round(df ['close'][0], 2)

''' today, today - quarter, today - quarter * 2, today - quarter * 3 '''
def get_h_price_list(stock_code, today):
	data_list = []

	q1 = today
	q2 = q1 - datetime.timedelta(days=91)
	q3 = q2 - datetime.timedelta(days=91)
	q4 = q3 - datetime.timedelta(days=91)

	d1 = get_h_data(stock_code, q1)
	d2 = get_h_data(stock_code, q2)
	d3 = get_h_data(stock_code, q3)
	d4 = get_h_data(stock_code, q4)

	data_list.append(d1)
	data_list.append(d2)
	data_list.append(d3)
	data_list.append(d4)

	return data_list

if __name__ == '__main__':
	today = datetime.date.today()
	price_list = get_h_price_list('002337', today)
	print price_list


