# coding:utf-8
import re,os,sys,time
import requests,urllib2
import pdfkit
from lxml import etree

IF='if.html'
OF='of.html'

base_url='https://developer.android.com/guide/index.html?hl=zh-cn'
req=requests.get(base_url)
pg=etree.HTML(req.text)
lis=pg.xpath('//li[@class="nav-section"]')
pn=0
ugot=[]

def strip_box(IF,OF):
	ifp,ofp=open(IF, 'r'),open(OF,'a')
	for line in ifp.readlines():
		if (re.match('.*footer class.*', line)):
			break
		ofp.write(line)
	ifp.close()
	ofp.close()

def save_html(IF,text):
	ifp=open(IF,'a')
	#ifp.write(text.encode('utf-8'))
	ifp.write(text)
	ifp.close()

def url2pdf(url,pn):
	url=url.rstrip('\n')
	print("pn=%s: url=%s"%(pn,url))
	out='newdir/api_'+str(pn)+'.pdf'
	#text=requests.get(url).text
	try:
		text=urllib2.urlopen(url,timeout=5).read()
		save_html(IF,text)
		strip_box(IF,OF)
	except:
		pass
	
	try:
		pdfkit.from_file(OF,out)
	except:
		pass
	
	try:
		os.unlink(IF)
		os.unlink(OF)
	except:
		pass

if __name__ == "__main__":
	ufp=open('ulist', 'r')
	for idx,url in enumerate(ufp.readlines()):
		if not os.path.exists('newdir/api_'+str(idx)+'.pdf'):
			print('idx:%s not exist!'%idx)
			try:
				url2pdf(url,idx)
			except:
				print('idx:%s,url[%s] op failed!'%(idx,url))
				pass
			#time.sleep(5)
