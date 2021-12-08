from unittest import TestCase

import requests

from config.settings import env


class TestScraper(TestCase):

	def test_env_file_loads(self):
		self.assertIn('BASE_URL', env)

	def test_base_url_response_200(self):
		resp = requests.get(env['BASE_URL'])
		self.assertEqual(resp.status_code, 200)
