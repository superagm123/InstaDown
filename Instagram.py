import requests 
from requests import RequestException
from bs4 import BeautifulSoup


class Instagram:

	def request_data(self,url):
		try:
			response = requests.get(url)
			url_content = response.text
			return url_content
		except RequestException:
			return None

	def get_picture(self,url_content):
		soup = BeautifulSoup(url_content, 'lxml')
		url_picture = soup.find('meta', property='og:image')
		return url_picture['content']

	def get_picture_content(self,url_picture):
		requested_picture = requests.get(url_picture)
		return requested_picture.content

