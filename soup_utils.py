import requests
from bs4 import BeautifulSoup

def get_soup(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.content, 'html.parser')
