from bs4 import BeautifulSoup

html_sample = '<html>\
<body>\
	<h1 id = "title"> hello world </h1>\
	<a href = "http://www.bisu.edu.cn"> this is link1 </a>\
	<a href = "www.bisu.edu.cn"> this is link2 </a>\
	</body>							\
</html>'

soup = BeautifulSoup(html_sample,"html.parser")

#soup2 = BeautifulSoup(''.join(html_sample),"html.parser")
#print(soup2)

#soup 选择标签的方法
header = soup.select('h1');
print(header)
print(header[0])
print(header[0].text)


#soup 选择标签的方法

alink = soup.select('a')
print(alink)
print(alink[0])
print(alink[0].text)


#用for的方法轮询soup选择出来的集合

for link in alink:
	print(link.text)
	print(link['href'])


print(soup.text)

