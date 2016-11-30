#coding=utf-8  
#!/usr/bin/python  
# Filename : datetime_l.py

import datetime

today = datetime.date.today()
print 'today : ' + str(today)

d1 = datetime.date(2016, 11, 30)
d2 = datetime.date(2016, 8, 31)
d3 = d2 - datetime.timedelta(days=91)

print d1
print d2
print d3
print (d1-d2)
print ((d1-d2).days)