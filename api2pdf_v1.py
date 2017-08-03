# coding:utf-8
import re
import requests
from lxml import etree

base_url='https://developer.android.com/guide/index.html?hl=zh-cn'

req=requests.get(base_url)
pg=etree.HTML(req.text)

title=pg.xpath('//div[@class="nav-section-header"]/a/@href')

lis=pg.xpath('//li[@class="nav-section"]')

fp=open('url.txt', 'a+')

for li in lis:
	li_h_url=li.xpath('div/a/@href')[0]
	li_h_nam=li.xpath('div/a/text()')[0]
	fp.write(li_h_url+'\n')
	#fp.write(li_h_nam+'\n')
	for li_b in li.xpath('ul/li/a'):
		li_b_url=li_b.xpath('@href')[0]
		li_b_nam=li_b.xpath('text()')[0]
		fp.write(li_b_url+'\n')
		#fp.write(li_b_nam+'\n')
	fp.write('\n')
