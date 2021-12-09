from unittest import TestCase

import requests
from bs4 import BeautifulSoup

from config.settings import env
from main import Scraper


class TestScraper(TestCase):

	def test_env_file_loads(self):
		self.assertIn('BASE_URL', env)

	def test_base_url_response_200(self):
		resp = requests.get(env['BASE_URL'], headers={'User-Agent': env['USER_AGENT']})
		self.assertEqual(resp.status_code, 200)

	def test_base_url_expected_content(self):
		resp = requests.get(env['BASE_URL'], headers={'User-Agent': env['USER_AGENT']})
		soup = BeautifulSoup(resp.content, 'html.parser')
		realestate_searchbar = soup.find_all('div', attrs={'class': 'hero-content'})
		self.assertTrue(realestate_searchbar)

	def test_base_query_response_200(self):
		query_url = "list-1?boundingBox=-37.6,144.62,-38.45,145.36"
		resp = requests.get(f"{env['BASE_URL']}{query_url}")
		self.assertEqual(resp.status_code, 200)

	def test_base_query_expected_content(self):
		query_url = "list-1?boundingBox=-37.6,144.62,-38.45,145.36"
		resp = requests.get(f"{env['BASE_URL']}{query_url}", headers={'User-Agent': env['USER_AGENT']})
		soup = BeautifulSoup(resp.content, 'html.parser')
		realestate_content = soup.find_all('div', attrs={'class': 'layout__content'})
		self.assertTrue(realestate_content)

	def test_Scraper_parses_first_page(self):
		s = Scraper(env['BASE_URL'])
		query_url = "list-1?boundingBox=-37.6,144.62,-38.45,145.36"
		s.get_content(query_url)
		soup = s.parse_content()
		content_div = soup.find('div', attrs='layout__content')
		self.assertTrue(content_div)
