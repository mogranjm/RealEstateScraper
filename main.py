# import requests
import re

import requests

from bs4 import BeautifulSoup

from config.settings import env


class Scraper:

	def __init__(self, base_url):
		self.base_url = base_url

		self.headers = {
			'User-Agent': env['USER_AGENT']
		}

		self.current_url = None
		self.next_url = None
		self.page_content = None
		self.scraped_data = None
		self.page_count = None

	def get_content(self, query_url):
		full_url = f"{self.base_url}{query_url}"
		request = requests.get(full_url, headers=self.headers)

		soup = BeautifulSoup(self.content, 'html.parser')
		self.listings = soup.find_all('li', attrs={'data-testid': re.compile("listing.+|topspot")})
		self.next_page_url = soup.find_all('a', attrs={'data-testid': 'paginator-navigation-button'})[-1]['href']
		self.page_content = request.content

	def parse_listings(self):
		return soup

	def extract_data(self, content_dict, soup):
		results =
		return results

	def next_page(self, current_page):
		wait = random.uniform(30, 60)
		self.current_url
		pass

	def write_data(self):
		pass

	def search(self, query):
		pass

if __name__ == '__main__':
	base_url = env['BASE_URL']

	greater_melbourne_query_url = "list-1?boundingBox=-37.6,144.62,-38.45,145.36"

	scraper = Scraper(base_url)
	Scraper.get_content(greater_melbourne_query_url)