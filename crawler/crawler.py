#coding=utf-8  
#!/usr/bin/python  
# Filename : crawler.py

import time
import pack
import roe
import profit_year
import shutil
import os

def main():
    line = [line.rstrip() for line in open('./data/stock_list')]
    
    stock_dict = {}
    global stock_dict

    for item in line:
                pack_content = pack.get_content(pack.get_url((item)))
    	roe_content = roe.get_content(roe.get_url((item)))
                profit_year_content = profit_year.get_content(profit_year.get_url(item))

    	# print '\n\n'
    	# print pack.get_date_data(pack_content)
    	# print pack.get_profit_data(pack_content)
    	# print pack.get_revenue_data(pack_content)
    	# print roe.get_roe_data(roe_content)
                # print profit_year.get_profit_data(profit_year_content)

    	stock_list = []
    	stock_list.append(pack.get_date_data(pack_content))
    	stock_list.append(pack.get_profit_data(pack_content))
    	stock_list.append(pack.get_revenue_data(pack_content))
    	stock_list.append(roe.get_roe_data(roe_content))
                stock_list.append(profit_year.get_profit_data(profit_year_content))
    	# print stock_list

    	global stock_dict
    	stock_dict[item] = stock_list
                print 'INFO: Crawling stock [' + item +']'
    	# print stock_dict


    file_name = './data/stock_data_' + time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    stock_data = open(file_name, "w+")
    stock_data.write(str(stock_dict))
    stock_data.close()
    print 'INFO: New Stock File [' + file_name + ']'

    file_name_new = './data/stock_data_new'
    if os.path.isfile(file_name_new):
        print 'INFO: Delete File [' + file_name_new + ']'
        os.remove(file_name_new)
        time.sleep(2)

    print 'INFO: Copy File From [' + file_name + '] To [' + file_name_new + ']'
    shutil.copy(file_name, file_name_new)

    # print file_name
    # print file_name_new