#coding=utf-8  
#!/usr/bin/python  
# Filename : roe.py

import urllib2
import sys
import re
import time

reload(sys)
sys.setdefaultencoding('utf-8')

def get_type(symbol):
	if symbol[0] == '6':
		return 'sh' + symbol

	return 'sz' + symbol

def get_url(symbol):
    url = 'http://quote.eastmoney.com/' + get_type(symbol) + '.html?stockcode=' + symbol
    return url

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

def get_roe_data(html_content):
    w1 = 'class="hxsjccsyl"></b></a>'
    w2 = '%</td>'
    pattern = re.compile(w1 + '(.*?)' + w2, re.S)

    tables = None
    tables = pattern.findall(html_content)
    if tables is None:
        print 'Error: tables is null or no content'
        return None

    for table in tables:
        array = table[2:]
        return array

if __name__ == '__main__':
    line = [line.rstrip() for line in open('../data/stock_list')]
    
    for item in line:
    	content = get_content(get_url((item)))
    	print get_roe_data(content)
