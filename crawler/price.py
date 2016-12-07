import pandas as pd
import tushare as ts
import datetime
import time
import os
import shutil

def main():
	line = [line.rstrip() for line in open('data/stock_list')]
	for item in line:
		df = ts.get_h_data(item, start='1990-01-01')
		file_name = './data/price/' + item + '.csv'
		df.to_csv(file_name)
		print 'INFO: Price Info Downloaded [' + file_name + ']'