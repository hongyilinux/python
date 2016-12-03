from bs4 import BeautifulSoup
import requests

html_sample = '\
<html>\
<body>\
<h1 id = "title"> Hello python </h1>\
<a href = "http://www.bisu.edu.cn">this is link1</a>\
<a href = "http://www.163.com"> this is link2</a>\
</body>\
</html>'

soup = BeautifulSoup(html_sample,"html.parser")

header = soup.select('h1')
print(header[0].text)




