import requests 
from bs4 import BeautifulSoup

res = requests.get('http://www.bisu.edu.cn/')
res.encoding = 'utf-8'

soup = BeautifulSoup(res.text,"html.parser")

alink = soup.select('.yaowenlb')

for link in alink:
	print(link.select('span')[0].text)
	print(link.select('a')[0].text)
	print(link.select('a')[0]['href'])


