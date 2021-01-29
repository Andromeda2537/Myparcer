import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool


def get_url(url):
    """response in html format"""
    response = requests.get(url)
    return response.text


def all_links_on_models(html):
    """links to all models"""
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find('div', class_="js_wrapper_items")
    return links


def find_all(html):
    soup = BeautifulSoup(html, 'lxml')
    linkss = soup.find('a', class_="thumb shine").get('href')
    return linkss


print(find_all(get_url('https://gastronomia.by/catalog/svezhaya_vypechka/khleb')))
