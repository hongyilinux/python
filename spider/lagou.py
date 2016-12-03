import requests

from bs4 import BeautifulSoup

def main():
	headers = {
			'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
			'Host':'www.lagou.com',
					
		}
	result  = requests.get('https://www.lagou.com/jobs/list_python?px=default&city=%E5%8C%97%E4%BA%AC',headers = headers)
	print(result.content)

if __name__ == '__main__':
	main()




