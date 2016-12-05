import pandas as pd
import tushare as ts
import datetime
import time
import os
import shutil

if __name__ == '__main__':
	today = datetime.date.today()
	q1 = today
	q2 = q1 - datetime.timedelta(days=91)
	q3 = q2 - datetime.timedelta(days=91)
	q4 = q3 - datetime.timedelta(days=91)


