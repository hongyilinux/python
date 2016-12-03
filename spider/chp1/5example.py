import requests
from bs4 import  BeautifulSoup

res = requests.get('http://news.sina.com.cn/china/')
res.encoding = 'utf-8'

soup = BeautifulSoup(res.text,"html.parser")

alink = soup.select('.news-item');

for link in alink:
	if len(link.select('h2'))> 0 :
		print(link.select('h2')[0].text)
		print(link.select('.time')[0].text)
		print(link.select('a')[0]['href'])


