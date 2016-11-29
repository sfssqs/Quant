#coding=utf-8  
#!/usr/bin/python  
# Filename : date.py 

import urllib2
import sys
import re
import time

reload(sys)
sys.setdefaultencoding('utf-8')

def get_type(symbol):
	if symbol[0] == '6':
		return '01'

	return '02'

def get_url(symbol):
	return 'http://f10.eastmoney.com/f10_v2/BackOffice.aspx?command=RptF10MainTarget&code=' + \
		str(symbol) + get_type(symbol) +'&num=9&code1=sh' + str(symbol) + '&spstr=&n=2'

def get_content(url):
	for i in range(3):
		content = get_html_content(url)
		if content is not None:
			return content

		time.sleep(2)
		print 'WARNNING: Retry because html content is None'
	return None		

def get_html_content(url):
	if url is None:
		print 'ERROR: url is None'
		return

	request = None
	request = urllib2.Request(url)
	request.add_header('User-Agent','fake-client')
	if request is None:
		print 'ERROR: request is None'
		return

	response = None
	try:    
		response = urllib2.urlopen(request)
	except urllib2.URLError, e:    
		if hasattr(e,"code"):        
			print u"failed, reason : ", e.reason

	if response is None:
		print 'ERROR: response is None'
		return

	content = None
	content = response.read()
	if content is None:
		print 'ERROR: html content is None'
		return content

	return content
			
def get_date_data(html_content):
	w1 = '成长能力指标'
	w2 = '营业总收入'
	pattern = re.compile(w1 + '(.*?)' + w2, re.S)

	tables = None
	tables = pattern.findall(html_content)
	if tables is None:
		print 'ERROR: tables is None or no content'
		return None

	for table in tables:
		t1 = '<span>'
		t2 = '</span>'
		patt = re.compile( t1 + '(.*?)' + t2, re.S)
		array = patt.findall(table)
		return array

def get_profit_data(html_content):
    w1 = '扣非净利润'
    w2 = '营业总收入同比增长'
    pattern = re.compile(w1 + '(.*?)' + w2, re.S)

    tables = None
    tables = pattern.findall(html_content)
    if tables is None:
        print 'Error: tables is null or no content'
        return None

    for table in tables:
        t1 = '<span>'
        t2 = '</span>'
        patt = re.compile(t1 + '(.*?)' + t2, re.S)
        array = patt.findall(table)
        return array

def get_revenue_data(html_content):
	w1 = '营业总收入同比增长'
	w2 = '归属净利润同比增长'
	pattern = re.compile(w1+'(.*?)'+w2,re.S)

	tables = None
	tables = pattern.findall(html_content)
	if tables is None:
		print 'ERROR: tables is null or no content'
		return None

	for table in tables:
		t1 = '<span>'
		t2 = '</span>'
		patt = re.compile(t1 + '(.*?)' + t2,re.S)
		array = patt.findall(table)
		return array

if __name__ == '__main__':
    line = [line.rstrip() for line in open('../data/stock_list')]
    
    for item in line:
    	content = get_content(get_url((item)))
    	print get_date_data(content)
    	print get_profit_data(content)
    	print get_revenue_data(content)

    	# get_content(item)
    	# time.sleep(2)


	