#coding=utf-8  
#!/usr/bin/python  

import os
import time
import sys, os, os.path, re, urllib, urlparse  
import smtplib  
import traceback  
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart  
 
def sendmail(subject, msg, toaddrs, fromaddr, smtpaddr, password):  
	''''' 
	@subject:\u90ae\u4ef6\u4e3b\u9898 
	@msg:\u90ae\u4ef6\u5185\u5bb9 
	@toaddrs:\u6536\u4fe1\u4eba\u7684\u90ae\u7bb1\u5730\u5740 
	@fromaddr:\u53d1\u4fe1\u4eba\u7684\u90ae\u7bb1\u5730\u5740 
	@smtpaddr:smtp\u670d\u52a1\u5730\u5740\uff0c\u53ef\u4ee5\u5728\u90ae\u7bb1\u770b\uff0c\u6bd4\u5982163\u90ae\u7bb1\u4e3asmtp.163.com 
	@password:\u53d1\u4fe1\u4eba\u7684\u90ae\u7bb1\u5bc6\u7801 
	a'''  
	mail_msg = MIMEMultipart()  
	if not isinstance(subject,unicode):  
		subject = unicode(subject, 'utf-8')
	mail_msg['Subject'] = subject  
	mail_msg['From'] =fromaddr  
	mail_msg['To'] = ','.join(toaddrs)  
	mail_msg.attach(MIMEText(msg, 'html', 'utf-8'))  

	# Attachment file
	#attach = MIMEText(open('price_data.zip', 'rb').read(), 'base64', 'utf-8')    
	#attach["Content-Type"] = 'application/octet-stream'    
	#attach["Content-Disposition"] = 'attachment; filename="price_data.zip"'    
	#mail_msg.attach(attach)

	try:  
		s = smtplib.SMTP()  
		s.connect(smtpaddr)  #\u8fde\u63a5smtp\u670d\u52a1\u5668  
		s.login(fromaddr,password)  #\u767b\u5f55\u90ae\u7bb1  
		s.sendmail(fromaddr, toaddrs, mail_msg.as_string()) #\u53d1\u9001\u90ae\u4ef6  
		s.quit()  
	except Exception,e:  
		print "Error: unable to send email"  
		print traceback.format_exc()  

if __name__ == '__main__':
	while(1):
		if not os.path.exists('data/603887.csv'):
			time.sleep(60)
			print 'sleep for 60 seconds'
		else:  
			break
 	      
	fromaddr = "sfssqs@163.com"  
	smtpaddr = "smtp.163.com"  
	toaddrs = ["xiaxingwork@163.com"]  
	subject = "AutoMail: Stocks Price Info"  
	password = "123abc"  
	msg = "Content is null"
	sendmail(subject,msg,toaddrs,fromaddr,smtpaddr,password)