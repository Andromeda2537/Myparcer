import requests
from bs4 import BeautifulSoup
import time


def get_url(url):
    response = requests.get(url)
    return response.text


def all_links(html):
    soup = BeautifulSoup(html, 'lmxl')
    links = soup.find('div', id="bx_1847241719_88")
